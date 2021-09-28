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

    driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
    driver.get(url)
    price = driver.find_element_by_id("price_inside_buybox").text
    name = driver.find_element_by_id(id_="productTitle").text
    # get only the first 20 chars of the name

    driver.close()
    return [price, name[:20]]


def notifyClient(old_price, new_price, name):
    notify = Notify()
    notify.title = "Price Has Change"
    notify.message = "{}: From {} to {}".format(name, old_price, new_price)
    notify.send()


class TrackerProduct:
    def __init__(self, url):
        self.url = url
        self.old_price = None
        self.new_price = get_price(self.url)[0]
        self.name = get_price(self.url)[1]
        self.notifyClient = notifyClient
        self.first_run = True

    def track(self):
        while True:
            print("ECO")
            new_price = get_price(self.url)
            if new_price != self.old_price:
                self.notifyClient(self.old_price, new_price, self.name)
                self.old_price = new_price
            else:
                self.notifyClient(self.old_price, new_price, self.name)
                self.old_price = new_price
            sleep(10)

    def start(self):
        self.track()


product1 = TrackerProduct(
    "https://www.amazon.com/AmazonBasics-Performance-Alkaline-Batteries-Count/dp/B00MNV8E0C/ref=sr_1_3?dchild=1&keywords=amazonbasics&pd_rd_r=6c60c00b-78c8-4315-98de-889051ec005c&pd_rd_w=UEFh5&pd_rd_wg=6D8OT&pf_rd_p=9349ffb9-3aaa-476f-8532-6a4a5c3da3e7&pf_rd_r=P2SBCQ0EQ1XH2MEBZS54&qid=1632772274&sr=8-3",
).start()
