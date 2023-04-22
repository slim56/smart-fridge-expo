from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as kyprops
# from sms import *  # when I run the GUI the message sends while the GUI is loading up.
import datetime
import calendar

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.greeting = Label(

            text="Welcome to Our Exhibit",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.greeting)
        self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_2 = Button(
            text="Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_2.bind(on_press=self.on_button_2_click)
        self.layout.add_widget(self.button_2)

        self.button_3 = Button(
            text="Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color="blue",
            background_normal=""
        )
        self.button_3.bind(on_press=self.on_button_3_click)
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="green",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Sensor 1"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Calendar"

class Sensor1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.greeting = Label(
            text="Info for Sensor 1!",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.greeting)
        self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_1 = Button(
            text="MainScreen",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_1.bind(on_press=self.on_button_1_click)
        self.layout.add_widget(self.button_1)

        self.button_3 = Button(
            text="Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color="blue",
            background_normal=""
        )
        self.button_3.bind(on_press=self.on_button_3_click)
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="green",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_1_click(self, instance):
        app = App.get_runni1button_1g_app()
        app.screen_manager.current = "MainScreen"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Calendar"

class Sensor2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.greeting = Label(
            text="Info for Sensor 2!",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.greeting)
        self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_1 = Button(
            text="MainScreen",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_1.bind(on_press=self.on_button_1_click)
        self.layout.add_widget(self.button_1)

        self.button_2 = Button(
            text="Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color="blue",
            background_normal=""
        )
        self.button_2.bind(on_press=self.on_button_2_click)
        self.layout.add_widget(self.button_2)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="green",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_1_click(self, instance):
        app = App.get_runni1button_1g_app()
        app.screen_manager.current = "MainScreen"

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Sensor 1"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.screen_manager.current = "Calendar"

class Reminder:
    def __init__(self, date, message):
        self.date = date
        self.message = message

class calendarScreen(Screen):
    header = kyprops
    reminder_label = kyprops
    reminder_entry = kyprops
    selected_date = None
    reminders = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
         # create calendar and set current date
        self.cal = calendar.Calendar()
        now = datetime.datetime.now()
        self.year = now.year # you can change this to current year
        self.month = now.month # you can change this to current month
        self.selected_date = None
        self.layout = GridLayout()
        self.layout.cols = 7
        self.spacing = [2,2]

        # shows the current month
        self.header = Label(text=f"{calendar.month_name[self.month]} {self.year}")
        self.add_widget(self.header)
        self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        # # shows the week and days
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


class SmartFridge(App):
    def build(self):
        self.sm = ScreenManager()
        self.main_screen = MainScreen(name="MainScreen")
        self.Sensor_1 = Sensor1(name="Sensor 1")
        self.Sensor_2 = Sensor2(name="Sensor 2")
        self.Calendar = calendarScreen(name="Calendar")
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.Sensor_1)
        self.sm.add_widget(self.Sensor_2)
        self.sm.add_widget(self.Calendar)
        return self.sm


if __name__ == "__main__":
    SmartFridge().run()