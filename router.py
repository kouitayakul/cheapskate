#Import Twilio packages
from twilio.rest import Client
# Enables us to send emails
import smtplib

# ehlo sends by an email server to identify itself when connecting 
# to another email server to start the process of sending an email
# starttls encrypts our connection
def send_email(subMsg, bodyMsg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('kouitayakul@gmail.com', 'sqxycebybtcwacuq')
    subject = subMsg
    body = bodyMsg
    msg = 'Subject: %s\n\n%s' % (subject, body)

    server.sendmail(
        'kouitayakul@gmail.com',
        'kouitayakul@gmail.com',
        msg
    )
    print('Email successfully sent!')

    server.quit()

def send_text(subMsg, bodyMsg):
    twilio_Sid = 'your Twilio sid'
    twilio_Auth_Token = 'your Twilio auth token'

    # Creating twilio client with our credentials
    whatsApp_Client = Client(twilio_Sid, twilio_Auth_Token)

    contacts = {
        'number': 'phone number'
    }

    for key, value in contacts.items():
        try:
            notify_msg = whatsApp_Client.messages.create(
                body = subMsg + bodyMsg,
                from_= 'whatsapp:+14155238886',
                to = 'whatsapp:' + value
            )
        except:
            print('Error occured while sending text')
        
        print('WhatsApp message successfully sent to %s' % notify_msg.to)
        print(notify_msg.sid)