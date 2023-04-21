import tkinter as tk
import calendar

class Reminder:
    def __init__(self, date, message):
        self.date = date
        self.message = message

class CalendarGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar with Reminders")

        # create calendar and set current date
        self.cal = calendar.Calendar()
        self.year = 2023 # you can change this to current year
        self.month = 4 # you can change this to current month
        self.selected_date = None

        # create reminder dictionary
        self.reminders = {}

        # create calendar header
        self.header = tk.Label(master, text=f"{calendar.month_name[self.month]} {self.year}", font=("Arial", 20))
        self.header.grid(row=0, column=0, columnspan=7)

        # create day labels
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label = tk.Label(master, text=day, font=("Arial", 12))
            label.grid(row=1, column=i)

        # create calendar days
        self.buttons = {}
        for week_num, week in enumerate(self.cal.monthdayscalendar(self.year, self.month), start=2):
            for day_num, day in enumerate(week):
                if day != 0:
                    button = tk.Button(master, text=str(day), font=("Arial", 12))
                    button.grid(row=week_num, column=day_num,padx=2, pady=2, sticky="nsew")
                    button.bind("<Button-1>", self.select_date)
                    self.buttons[(day, week_num, day_num)] = button

        # create reminder input
        self.reminder_label = tk.Label(master, text="Reminder: ")
        self.reminder_label.grid(row=8, column=0)
        self.reminder_entry = tk.Entry(master)
        self.reminder_entry.grid(row=8, column=1)
        self.add_button = tk.Button(master, text="Add Reminder", command=self.add_reminder)
        self.add_button.grid(row=8, column=2)

    def select_date(self, event):
        # unselect previous date
        if self.selected_date:
            self.buttons[self.selected_date].config(relief=tk.RAISED)

        # select new date
        widget = event.widget
        widget.config(relief=tk.SUNKEN)
        day = int(widget["text"])
        row, col = widget.grid_info()["row"]-2, widget.grid_info()["column"]
        self.selected_date = (day, row, col)

        # update header with selected date
        date = calendar.date(self.year, self.month, day)
        self.header.config(text=date.strftime("%A, %B %d, %Y"))

        # show reminders for selected date
        if self.selected_date in self.reminders:
            reminder_text = "\n".join(self.reminders[self.selected_date])
        else:
            reminder_text = "No reminders"
        self.reminder_label.config(text=f"Reminders for {date.strftime('%B %d, %Y')}:")
        self.reminder_entry.delete(0, tk.END)
        self.reminder_entry.insert(0, reminder_text)

    def add_reminder(self):
        if self.selected_date:
            reminder = self.reminder_entry.get()
            if self.selected_date not in self.reminders:
                self.reminders[self.selected_date] = []
            self.reminders[self.selected_date].append(reminder)
            self.select_date(tk.Event())

root = tk.Tk()
app = CalendarGUI(root)
root.mainloop()