from notifypy import Notify


# simple notification
notifcation = Notify()
notifcation.title = "cool title"
notifcation.message = "something amazing"
notifcation.send()

# # notification with icon
# notifcation = Notify()
# notifcation.title = "cool title"
# notifcation.message = "something amazing"
# notifcation.icon = "path/to/OPEN.png"
# notifcation.send()

# notification with audio
# notifcation = Notify()
# notifcation.title = "cool title"
# notifcation.message = "something amazing"
# notifcation.audio = ""
# notifcation.send()