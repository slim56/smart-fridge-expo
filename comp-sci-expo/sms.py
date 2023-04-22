# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import datetime
from time import sleep
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC11df50ad48a78033121c05277ab51668"
auth_token = "589fb3caa9812d9df7af7e275c7bd364"
client = Client(account_sid, auth_token)

# Set the date and time to send the message
hour = 15 # military time
minute = 18
send_date = datetime.datetime(2023, 4, 20, hour, minute, 0)

# Wait until the specified date and time
while datetime.datetime.now() < send_date:
    pass

message = client.messages.create(
  body="Hello from The other side",
  from_="+18449862899",
  media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
  to="+19857134658"
)
print(message.sid)