from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import kivy.properties as kyprops
import calendar

class Reminder:
    def __init__(self, date, message):
        self.date = date
        self.message = message

class CalendarGUI(GridLayout):
    header = kyprops
    reminder_label = kyprops
    reminder_entry = kyprops
    selected_date = None
    reminders = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 7
        self.spacing = [2,2]

        # create calendar and set current date
        self.cal = calendar.Calendar()
        self.year = 2023 # you can change this to current year
        self.month = 4 # you can change this to current month

        # create calendar header
        self.header = Label(text=f"{calendar.month_name[self.month]} {self.year}", font_size=20)
        self.add_widget(self.header)

        # create day labels
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in days:
            label = Label(text=day, font_size=12, size_hint_y=None, height=50)
            self.add_widget(label)

        # create calendar days
        for week in self.cal.monthdayscalendar(self.year, self.month):
            for day in week:
                if day != 0:
                    button = Button(text=str(day), font_size=12, size_hint_y=None, height=50)
                    button.bind(on_press=self.select_date)
                    self.add_widget(button)

        # create reminder input
        self.reminder_label = Label(text="Reminder: ")
        self.add_widget(self.reminder_label)
        self.reminder_entry = Label()
        self.add_widget(self.reminder_entry)

    def select_date(self, instance):
        # unselect previous date
        if self.selected_date:
            self.selected_date.background_color = [1,1,1,1]

        # select new date
        instance.background_color = [0.5,0.5,1,1]
        day = int(instance.text)
        self.selected_date = instance

        # update header with selected date
        date = calendar.date(self.year, self.month, day)
        self.header.text = date.strftime("%A, %B %d, %Y")

        # show reminders for selected date
        if self.selected_date in self.reminders:
            reminder_text = "\n".join(self.reminders[self.selected_date])
        else:
            reminder_text = "No reminders"
        self.reminder_label.text = f"Reminders for {date.strftime('%B %d, %Y')}:"
        self.reminder_entry.text = reminder_text

    def add_reminder(self):
        if self.selected_date:
            reminder = self.reminder_entry.text
            if self.selected_date not in self.reminders:
                self.reminders[self.selected_date] = []
            self.reminders[self.selected_date].append(reminder)
            self.select_date(self.selected_date)

class CalendarApp(App):
    def build(self):
        return CalendarGUI()

if __name__ == '__main__':
    CalendarApp().run()

