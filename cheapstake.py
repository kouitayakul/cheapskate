# allow us to access the url and pull information from any website
import requests
# Extracts all data from the webpage
from bs4 import BeautifulSoup
# Enanles us to send emails
import smtplib

URL = 'https://www.amazon.ca/MuscleTech-NitroTech-Protein-Peptides-Chocolate/dp/B00BMEEVNK/ref=sr_1_8?keywords=protein+powder&qid=1574142455&sr=8-8'

# Identify the browser and operating system to the web server
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soupToUse = BeautifulSoup(soup.prettify(), 'html.parser')

    prodTitle = soupToUse.find(id='productTitle').get_text()
    titleStrip = prodTitle.strip()
    price = soupToUse.find(id='priceblock_ourprice').get_text()
    currentPrice = float(price[5:10])
    wishPrice = float((currentPrice - (currentPrice * .10)))

    print(currentPrice)
    print(titleStrip)

    if(currentPrice <= wishPrice):
        send_email()

# ehlo sends by an email server to identify itself when connecting 
# to another email server to start the process of sending an email

# starttls encrypts our connection
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('kouitayakul@gmail.com', 'sqxycebybtcwacuq')
    subject = 'Price has dropped!'
    body = 'Checkout this link: %s' % URL
    msg = 'Subject: %s\n\n%s' % (subject, body)

    server.sendmail(
        'kouitayakul@gmail.com',
        'kouitayakul@gmail.com',
        msg
    )
    print('Email successfully sent!')

    server.quit()

check_price()

