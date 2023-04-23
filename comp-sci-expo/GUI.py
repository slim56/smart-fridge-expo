from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
import calendar
from twilio.rest import Client

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
            background_color="red",
            background_normal=""
        )
        self.button_3.bind(on_press=self.on_button_3_click)
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 1"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"

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
            background_color="red",
            background_normal=""
        )
        self.button_3.bind(on_press=self.on_button_3_click)
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"

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
            background_color="red",
            background_normal=""
        )
        self.button_2.bind(on_press=self.on_button_2_click)
        self.layout.add_widget(self.button_2)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal=""
        )
        self.button_4.bind(on_press=self.on_button_4_click)
        self.layout.add_widget(self.button_4)

        self.add_widget(self.layout)

    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 1"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"

class Reminder:
    def __init__(self, date, message):
        self.date = date
        self.message = message

class calendarScreen(Screen):
    # header = kyprops
    # reminder_label = kyprops
    # reminder_entry = kyprops
    # selected_date = None
    reminders = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 7
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.layout.spacing = [4,4]

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        days_in_month = calendar.monthrange(year, month)[1]
        month_name = calendar.month_name[month]

        self.greeting = Label(
            text=f"{month_name} {year}",
            font_size=12,
            color=(1, 1, 1, 1)
        )
        self.layout.add_widget(self.greeting)

        # Create buttons for each day in the month
        self.day_buttons = []
        for i in range(1, days_in_month + 1):
            day = datetime.date(year, month, i)
            day_of_week = calendar.day_name[day.weekday()]
            day_button = Button(
                text=f"{day_of_week} {i}",
                background_color=(0, 0, 1, 1),
                background_normal="",
                on_press=self.on_day_button_click
            )
            day_button.bind(on_press=lambda instance, day=day: self.on_day_button_click(day))
            self.layout.add_widget(day_button)
            self.day_buttons.append(day_button)

        self.button_1 = Button(
            text="MainScreen",
            size_hint=(1, 0.5),
            bold=True,
            background_color=("red"),
            background_normal="",
            on_press=self.on_button_1_click
        )
        self.layout.add_widget(self.button_1)

        self.button_2 = Button(
            text="Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color=("red"),
            background_normal="",
            on_press=self.on_button_2_click
        )
        self.layout.add_widget(self.button_2)

        self.button_3 = Button(
            text="Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color=("red"),
            background_normal="",
            on_press=self.on_button_3_click
        )
        self.layout.add_widget(self.button_3)

        self.add_widget(self.layout)

        # # Set environment variables for your credentials
        # # Read more at http://twil.io/secure
        # account_sid = "AC11df50ad48a78033121c05277ab51668"
        # auth_token = ""
        # self.client = Client(account_sid, auth_token)

        # # Set the date and time to send the message
        # hour = 15 # military time
        # minute = 18
        # send_date = datetime.datetime(2023, 4, 20, hour, minute, 0)

        # # Wait until the specified date and time
        # while datetime.datetime.now() < send_date:
        #     pass

        # self.message = self.client.messages.create(
        #     body="Hello from The other side",
        #     from_="+18449862899",
        #     media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
        #     to="+19857134658"
        # )
        # print(self.message.sid)

    def on_day_button_click(self, instance):
        print(f"Clicked on {instance.text}")

    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 1"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 2"

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
