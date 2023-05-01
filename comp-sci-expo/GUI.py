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
        self.layout.spacing = [1,2]

        self.greeting = Label(

            text="Welcome to Our Project",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.greeting)
        self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_2 = Button(
            text="Weight Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_2_click
        )
        self.layout.add_widget(self.button_2)

        self.button_3 = Button(
            text="Weight Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_3_click
        )
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_4_click
        )
        self.layout.add_widget(self.button_4)

        self.close = Button(
            text="Close",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_close_click
        )
        self.layout.add_widget(self.close)

        self.add_widget(self.layout)

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Weight Sensor 1"
        
    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Weight Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"

    def on_close_click(self, instance):
        App.get_running_app().stop()
class Sensor1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.layout.spacing = [1,2]

        self.greeting = Label(
            text="Weight 1: Weight will be displayed  ",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.greeting)
        # self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_1 = Button(
            text="MainScreen",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_1_click
        )
        self.layout.add_widget(self.button_1)

        self.button_3 = Button(
            text="Weight Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_3_click
        )
        self.layout.add_widget(self.button_3)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_4_click
        )
        self.layout.add_widget(self.button_4)

        self.close = Button(
            text="Close",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_close_click
        )
        self.layout.add_widget(self.close)

        self.add_widget(self.layout)


    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Weight Sensor 2"

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"

    def on_close_click(self, instance):
        App.get_running_app().stop()

class Sensor2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout()
        self.layout.cols = 1
        self.layout.size_hint = (0.6, 0.7)
        self.layout.pos_hint = {"center_x":0.5, "center_y": 0.5}
        self.layout.spacing = [1,2]

        self.sensor_2 = Label(
            text="Weight 2: Weight will be displayed",
            font_size=18,
            color="white"
        )
        self.layout.add_widget(self.sensor_2)
        # self.layout.add_widget(Image(source="SMART FRIDGE.PNG"))

        self.button_1 = Button(
            text="MainScreen",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_1_click
        )
        self.layout.add_widget(self.button_1)

        self.button_2 = Button(
            text="Weight Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_2_click
        )
        self.layout.add_widget(self.button_2)

        self.button_4 = Button(
            text="Calendar",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_button_4_click
        )
        self.layout.add_widget(self.button_4)

        self.close = Button(
            text="Close",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_close_click
        )
        self.layout.add_widget(self.close)

        self.add_widget(self.layout)

    def on_button_1_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "MainScreen"

    def on_button_2_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Weight Sensor 1"
        # r1 = Reminder.__init__(self)

    def on_button_4_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Calendar"
    
    def on_close_click(self, instance):
        App.get_running_app().stop()
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

        # Create a new GridLayout to contain the month and year labels and the existing GridLayout
        main_layout = GridLayout(cols=1, size_hint=(0.8, 0.8), pos_hint={"center_x": 0.5, "center_y": 0.5})
        
        # Create a BoxLayout to contain the month and year labels
        header_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height='30dp')
        
        # Create the month and year labels
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        days_in_month = calendar.monthrange(year, month)[1]
        month_name = calendar.month_name[month]

        self.month_label = Label(
            text=f"{month_name} {year}",
            bold=True,
            font_size=24,
            color=("white"),
            size_hint=(1, None),
            height='30dp',
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        
        # Add the month and year labels to the header layout
        header_layout.add_widget(self.month_label)
        
        # Add the header layout and the existing GridLayout to the main layout
        main_layout.add_widget(header_layout)
        main_layout.add_widget(self.layout)
        
        # Add the main layout to the screen
        self.add_widget(main_layout)

        # # Create a new GridLayout for the title
        # title_layout = GridLayout(cols=1, size_hint=(0.5, 0.2))
        # title_layout.add_widget(Label(text=f"{month_name} {year}", font_size=20, bold=True))

        # # Add the new GridLayout to the main layout
        # self.layout.add_widget(title_layout)

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
            text="Weight Sensor 1",
            size_hint=(1, 0.5),
            bold=True,
            background_color=("red"),
            background_normal="",
            on_press=self.on_button_2_click
        )
        self.layout.add_widget(self.button_2)

        self.button_3 = Button(
            text="Weight Sensor 2",
            size_hint=(1, 0.5),
            bold=True,
            background_color=("red"),
            background_normal="",
            on_press=self.on_button_3_click
        )
        self.layout.add_widget(self.button_3)

        self.close = Button(
            text="Close",
            size_hint=(1, 0.5),
            bold=True,
            background_color="red",
            background_normal="",
            on_press=self.on_close_click
        )
        self.layout.add_widget(self.close)

        # self.add_widget(self.layout)

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

        # Phone_numbers= ["+19857134658", "+15044102192", "+13185642414"]
        self.client.messages.create(
            body=f"this is your reminder for your event/food",
            from_="+18449862899",
            to="+19857134658" # str(Phone_numbers)
            )

    def on_day_button_click(self, instance):
        try:
            year, month, day = str(instance).split("-")
            selected_date = datetime.datetime(month=int(month), day=int(day), year=int(year), hour=0, minute=0)

            # Create a popup to ask for the notification time
            popup = Popup(title='Experation Time',
                          size_hint=(None, None), size=(600, 400))
            label = Label(
                text='Enter Reminder Time and Name\n Millitary Time Ex:(14:30)',
                pos_hint={"center_x": 0.5, "center_y": 0.5}          
                          )

            # Define a custom input filter function that allows digits and colons
            def input_time(self, value, from_undo):
                if value.isdigit() or value == ":":
                    return value
                return ""
            def input_event(self, value, from_undo):
                if value.isalpha():
                    return
                return ""
            
            # input_box = TextInput(multiline=False, input_filter=input_event, size_hint_y=0.5)
            input_box_2 = TextInput(multiline=False, input_filter=input_time, size_hint_y=0.5)
            button = Button(text='OK', size_hint_y=0.5)
            button_2 = Button(text="Cancel", size_hint_y=0.5)

            # Bind the button to call the schedule method with the selected time and name of event
            button.bind(on_press=lambda *kwarg: (self.schedule(selected_date, datetime.datetime.strptime(input_box_2.text, '%H:%M').time()), popup.dismiss()))
            button_2.bind(on_press=popup.dismiss)
            # Add the widgets to the popup and display it
            popup.content = BoxLayout(orientation='vertical')
            popup.content.add_widget(label)
            # popup.content.add_widget(Label(text='Enter Name of Event', size_hint_y=None, height=20))
            # popup.content.add_widget(input_box)
            popup.content.add_widget(Label(text='Enter Time of Event:', size_hint_y=None, height=30))
            popup.content.add_widget(input_box_2)
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
        app.sm.current = "Weight Sensor 1"

    def on_button_3_click(self, instance):
        app = App.get_running_app()
        app.sm.current = "Weight Sensor 2"

    def on_close_click(self, instance):
        App.get_running_app().stop()

# This class takes the inputs of the buttons
# And swaps through the screens
class SmartFridge(App):
    def build(self):
        self.sm = ScreenManager()
        self.main_screen = MainScreen(name="MainScreen")
        self.Sensor_1 = Sensor1(name="Weight Sensor 1")
        self.Sensor_2 = Sensor2(name="Weight Sensor 2")
        self.Calendar = calendarScreen(name="Calendar")
        self.sm.add_widget(self.main_screen)
        self.sm.add_widget(self.Sensor_1)
        self.sm.add_widget(self.Sensor_2)
        self.sm.add_widget(self.Calendar)

        return self.sm


if __name__ == "__main__":
    SmartFridge().run()
