import calendar
import datetime
from kivy.app import App
from kivy.clock import Clock
from twilio.rest import Client
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

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
        # r1 = Reminder.__init__(self)
        
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
        # r1 = Reminder.__init__(self)

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"


# This class takes in the calendar class and uses the
# Twilio Api to make a calendar and sets reminders
class calendarScreen(Screen):

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = GridLayout()
        self.layout.cols = 7
        self.layout.size_hint = (0.8, 0.8)
        self.layout.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.layout.spacing = [4,4]

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        days_in_month = calendar.monthrange(year, month)[1]
        month_name = calendar.month_name[month]

        self.greeting = Label(
            text=f"{month_name} \n {year}",
            bold=True,
            font_size=12,
            color=("white")
        )
        self.layout.add_widget(self.greeting)

        # Create buttons for each day in the month
        self.day_buttons = []
        for i in range(1, days_in_month + 1):
            day = datetime.date(year, month, i)
            day_of_week = calendar.day_name[day.weekday()]
            day_button = Button(
                text=f"{day_of_week} \n{i}",
                background_color=("blue"),
                background_normal="",
                on_press=self.on_day_button_click
            )
            day_button.bind(on_press=lambda instance, day=day: self.on_day_button_click(day))
            self.layout.add_widget(day_button)

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

    def schedule(self, selected_date, notification_time):
        # Calculate the delay until the notification time
        notification_datetime = datetime.datetime.combine(selected_date.date(), notification_time)
        delay = (notification_datetime - datetime.datetime.now()).total_seconds()

        # Schedule the message to be sent after the delay
        Clock.schedule_once(self.send_message, delay)

    def send_message(self, dt):
        account_sid = "AC11df50ad48a78033121c05277ab51668"
        auth_token = ""
        self.client = Client(account_sid, auth_token)

        self.client.messages.create(
            body="Your Food has expired",
            from_="+18449862899",
            to="+19857134658"
            )

    def on_day_button_click(self, instance):
        try:
            year, month, day = str(instance).split("-")
            selected_date = datetime.datetime(month=int(month), day=int(day), year=int(year), hour=0, minute=0)

            # Create a popup to ask for the notification time
            popup = Popup(title='Experation Time',
                          size_hint=(None, None), size=(400, 200))
            label = Label(
                text='Enter the Experation Date (hh:mm):',
                pos_hint={"center_x": 0.5, "center_y": 0.5}          
                          )

            # Define a custom input filter function that allows digits and colons
            def input_filter(value, from_undo):
                if value.isdigit() or value == ":":
                    return value
                return ""
            
            input_box = TextInput(multiline=False, input_filter=input_filter, size_hint_y=0.5)
            button = Button(text='OK', size_hint_y=0.5)
            button_2 = Button(text="Cancel", size_hint_y=0.5)

            # Bind the button to call the schedule method with the selected time
            button.bind(on_press=lambda *args: (self.schedule(selected_date, datetime.datetime.strptime(input_box.text, '%H:%M').time())))
            button_2.bind(on_press=popup.dismiss)
            # Add the widgets to the popup and display it
            popup.content = BoxLayout(orientation='vertical')
            popup.content.add_widget(label)
            popup.content.add_widget(input_box)
            popup.content.add_widget(button)
            popup.content.add_widget(button_2)
            popup.open()
        except ValueError:
            pass

    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 1"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Sensor 2"

# This class takes the inputs of the buttons
# And swaps through the screens
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

if __name__ == "__main__":
    SmartFridge().run()
