from twilio.rest import Client
import flight_data

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message):

        account_sid = 'AC37911a60213a19cddcebb088716cb2d2'
        auth_token = '9de1faa512d6e3bafa5cc059ac57622e'
        client = Client(account_sid, auth_token)

        message = client.messages.create(body=message, from_= "+12137723903", to = '+420723251655')
        print(message.sid)

