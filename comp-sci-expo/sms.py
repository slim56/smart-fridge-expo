import os
from twilio.rest import Client
import datetime
from time import sleep

# Set environment variables for your credentials
account_sid = "AC11df50ad48a78033121c05277ab51668"
auth_token = ""
client = Client(account_sid, auth_token)


# this is an example of sending a message to more than on person
Phone_numbers= ["+19857134658", "+15044102192", "+13185642414"]
message = client.messages.create(
  body="wassup",
  from_="+18449862899",
  to= str(Phone_numbers)
)
print(message.sid)
