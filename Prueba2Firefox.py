from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--headless")

url = "https://zenbus.net/publicapp/web/limasanisidromibus77868410?line=677150016&stop=672740001&itinerary=822910079"

browser = webdriver.Firefox(GeckoDriverManager().install(),options=chrome_options)
browser.get(url)



while(True):
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    a = soup.find(class_="no-vehicle-content")
    if(a is not None):
        print(a.text)

