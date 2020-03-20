# Extracts all data from the webpage
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
import router
import helpers
import requests

URL = 'https://www.bestbuy.ca/en-ca/product/nba-2k20-ps4/13720461'
ua = UserAgent()
headers = {'User-Agent': ua.random}

# Subject and body for the message being sent
msgSubject = ''
msgBodyBuy = 'Go buy it now!: %s' % URL
msgBodyMaybe = 'Check out this link: %s' % URL


def check_price():
    # This helper allows us to perform a safer practice of web-scrapping but has a performance hit
    # page = helpers.getSoup()

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soupToUse = BeautifulSoup(soup.prettify(), 'html.parser')

    prodTitle = soupToUse.find(class_='productName_19xJx').get_text().strip()
    price = soupToUse.find(class_='price_FHDfG').get_text().strip()
    currentPrice = float(price[1:3]) + .99

    print(currentPrice)
    print(prodTitle)

    if(currentPrice < 40):
        msgSubject = 'Price has dropped! '
        router.send_email(msgSubject, msgBodyBuy)
        #router.send_text(msgSubject, msgBody)
    else:
        msgSubject = 'Still too expensive...($%s)' % currentPrice
        router.send_email(msgSubject, msgBodyMaybe)
        #router.send_text(msgSubject, msgBody)

check_price()


