import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import calendar
import datetime

class Reminder:
    def __init__(self, date, message):
        self.date = date
        self.message = message

class CalendarGUI(Screen):
    def __init__(self, **kwargs):
        super(CalendarGUI, self).__init__(**kwargs)
        self.name = 'calendar'

        # create calendar and set current date
        self.cal = calendar.Calendar()
        self.year = 2023 # you can change this to current year
        self.month = 4 # you can change this to current month
        self.selected_date = None

        # create reminder dictionary
        self.reminders = {}

        # create calendar header
        self.header = Label(text=f"{calendar.month_name[self.month]} {self.year}", font_size=20)
        self.add_widget(self.header)

        # create day labels
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        day_labels = GridLayout(cols=7, size_hint=(1, None), height=30)
        for day in days:
            label = Label(text=day, font_size=12)
            day_labels.add_widget(label)
        self.add_widget(day_labels)

        # create calendar days
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height-150))
        calendar_grid = GridLayout(cols=7, spacing=2, size_hint_y=None)
        calendar_grid.bind(minimum_height=calendar_grid.setter('height'))

        for week_num, week in enumerate(self.cal.monthdayscalendar(self.year, self.month), start=2):
            for day_num, day in enumerate(week):
                if day != 0:
                    button = Button(text=str(day), font_size=12, size_hint_y=None, height=60)
                    button.bind(on_press=self.select_date)
                    calendar_grid.add_widget(button)
                    self.buttons[(day, week_num, day_num)] = button

        scroll_view.add_widget(calendar_grid)
        self.add_widget(scroll_view)

        # create reminder input
        reminder_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.reminder_label = Label(text="Reminder: ")
        reminder_layout.add_widget(self.reminder_label)
        self.reminder_entry = TextInput()
        reminder_layout.add_widget(self.reminder_entry)
        self.add_widget(reminder_layout)

    def select_date(self, instance):
        # unselect previous date
        if self.selected_date:
            self.buttons[self.selected_date].state = 'normal'

        # select new date
        instance.state = 'down'
        day = int(instance.text)
        row, col = instance.grid_pos
        self.selected_date = (day, row, col)

        # update header with selected date
        date = datetime.date(self.year, self.month, day)
        self.header.text = date.strftime("%A, %B %d, %Y")

        # show reminders for selected date
        if self.selected_date in self.reminders:
            reminder_text = "\n".join(self.reminders[self.selected_date])
        else:
            reminder_text = "No reminders"
