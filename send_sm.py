# Download the helper library from https://www.twilio.com/docs/python/install
import os
#from getInfo import *
from twilio.rest import Client
from MainWindow import *

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
"""
account_sid = 'AC4f786eff34248408e94260ba0cbbf97d'
auth_token = 'e9b981f2ac30c03817e1318623143331'
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+15734848931',
         to='+18187990531'
     )

print(message.sid)
"""


# main()

def send_text(acc_sid, token, text):
    account_sid = acc_sid
    auth_token = token
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
             body=text,
            from_='+15734848931',
            to='+18187990531'
        )

    print(message.sid)