from notifypy import notify
import calendar
import datetime
import _strptime

yy = 2023
mm = 4

print(calendar.month(yy,mm,))

class Item:
    def __init__(self, weight, amount):
        self.weight = weight
        self.amount = amount

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        pass


class ExpirationDate:
    def __init__(self, year, month, day):
        self.expiration_date = datetime.date(year, month, day)

    def set_reminder(self):
        today = datetime.date.today()
        days_until_expiration = (self.expiration_date - today).days
        if days_until_expiration > 0:
            reminder_date = today + datetime.timedelta(days=days_until_expiration)
            print(f"Reminder set for {reminder_date}")
            self.show_calendar(reminder_date.year, reminder_date.month)
        else:
            print("Expiration date has already passed.")

    def show_calendar(self, year, month):
        cal = calendar.monthcalendar(year, month)
        print(calendar.month_name[month], year)
        print("Mo Tu We Th Fr Sa Su")
        for week in cal:
            week_str = ""
            for day in week:
                if day == 0:
                    week_str += "   "
                elif day == self.expiration_date.day:
                    week_str += f"({day:2d})"
                else:
                    week_str += f" {day:2d} "
            print(week_str)

    # def days_until_expiration():
    #     # Prompt the user to input a date
    #     date_str = input("Enter expiration date (YYYY-MM-DD): ")

    #     # Convert the user input to a datetime object
    #     expiration_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    #     # Calculate the number of days until the expiration date
    #     today = datetime.date.today()
    #     days_until_expiration = (expiration_date - today).days

    #     if days_until_expiration > 0:
    #         print(f"There are {days_until_expiration} days until the expiration date.")
    #     else:
    #         print("Expiration date has already passed.")
    # days_until_expiration()


class Notification:
    def __init__(self):
        pass

expiration_date = ExpirationDate(2023, 4, 30)
expiration_date.set_reminder()

# expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
# expiration_date_str = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()

# expiration_date.set_reminder()





