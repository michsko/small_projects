from twilio.rest import Client
import flight_data

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message):

        account_sid = 
        auth_token = 
        client = Client(account_sid, auth_token)

        message = client.messages.create(body=message, from_= "", to = '')
        print(message.sid)

