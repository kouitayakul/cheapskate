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
    twilio_Sid = 'AC2e45a7c61e8816c63ccd7fd23fa477fb'
    twilio_Auth_Token = '2166c759c7359fb7523f55ea770066f6'

    # Creating twilio client with our credentials
    whatsApp_Client = Client(twilio_Sid, twilio_Auth_Token)

    contacts = {
        'myself': '+17783209656'
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