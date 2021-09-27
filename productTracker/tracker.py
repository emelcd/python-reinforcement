from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from notifypy import Notify
from time import sleep

def get_price(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
    driver.get(url)
    price = driver.find_element_by_id('price_inside_buybox').text 
    driver.close()
    return price

def notifyClient(old_price, new_price):
    notify = Notify()
    if old_price == new_price:
        notify.title = "Price Has Change"
        notify.message = "From {} to {}".format(old_price, new_price)
        notify.send()
    else:
        notify.title = "Price Has Change"
        notify.message = "From {} to {}".format(old_price, new_price)
        notify.send()

class Tracker:
    def __init__(self, url, old_price):
        self.url = url
        self.old_price = old_price
        self.new_price = get_price(self.url)
        self.notifyClient = notifyClient

    def track(self):
        while True:
            print("ECO")
            new_price = get_price(self.url)
            if new_price != self.old_price:
                self.notifyClient(self.old_price, new_price)
                self.old_price = new_price
            else:
                pass
            sleep(10)

    def start(self):
        self.track()

# trackerProduct = Tracker('https://www.amazon.com/Lonyiabbi-Vibration-Interface-Product%EF%BC%88No-Installation/dp/B092QK7K5P/ref=sr_1_1_sspa?dchild=1&keywords=iron+man&qid=1632759118&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyMktFWUFRWENWWktQJmVuY3J5cHRlZElkPUEwMjg2MjIzMTVaUjRKQTlDS0JBTSZlbmNyeXB0ZWRBZElkPUEwMDcxMjUxM1EwRlVPS09IMTc3UiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=', '0')

# trackerProduct.start()   
    
while True:
    notification = Notify()
    notification.title = "Price Has Change"
    notification.message = "ECO"
    notification.send()
