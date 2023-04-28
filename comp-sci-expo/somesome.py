import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import ListProperty

class CalendarGrid(GridLayout):
    day_buttons = ListProperty([])

    def __init__(self, **kwargs):
        super(CalendarGrid, self).__init__(**kwargs)
        self.cols = 7
        for i in range(1, 32):
            button = Button(text=str(i), on_press=lambda day=i: self.set_reminder(day))
            self.add_widget(button)
            self.day_buttons.append(button)

    def set_reminder(self, day):
        # Create popup for user input
        popup = Popup(title=f"Set Reminder for Day {day}", size_hint=(0.8, 0.4))
        layout = GridLayout(cols=1)
        popup.add_widget(layout)
        reminder_input = TextInput(multiline=True)
        layout.add_widget(reminder_input)

        # Create save button
        def save_callback(instance):
            reminder = reminder_input.text
            if reminder:
                self.day_buttons[day-1].text = f"{day}\n{reminder}"
            popup.dismiss()
        save_button = Button(text="Set Reminder", on_press=save_callback)
        layout.add_widget(save_button)

        popup.open()

class CalendarApp(App):
    def build(self):
        return CalendarGrid()

if __name__ == '__main__':
    CalendarApp().run()
