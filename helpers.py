# allow us to access the url and pull information from any website
import requests
# Extracts all data from the webpage
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from itertools import cycle
import time

URL = 'https://www.bestbuy.ca/en-ca/product/nba-2k20-ps4/13720461'
proxyUrl = 'https://free-proxy-list.net/'
ua = UserAgent()
headers = {'User-Agent': ua.random}

def getProxies():
    page = requests.get(proxyUrl, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    soupToUse = BeautifulSoup(soup.prettify(), 'html.parser')
    
    tableRows = soupToUse.find(id='proxylisttable').find('tbody').find_all('tr')

    proxies_and_ports = set()

    for row in tableRows:
        cols = row.find_all('td')
        https = cols[6].get_text().strip()
        if(https == 'yes'):
            proxy = cols[0].get_text().strip()
            port = cols[1].get_text().strip()
            proxy_and_port = '%s:%s' % (proxy, port)
            proxies_and_ports.add(proxy_and_port)
    
    return proxies_and_ports


def getSoup():
    proxies = getProxies()
    proxies_cycle = cycle(proxies)

    for i in range(len(proxies)):
        proxy = next(proxies_cycle)
        try:
            page = requests.get(URL, headers=headers, proxies={'https': proxy})
            return page
        except:
            print('Error occured with proxy %s retrying with another proxy...' % proxy)
            time.sleep(15)