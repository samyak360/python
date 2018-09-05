#!/usr/bin/python

import time
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

res = requests.get("https://web.whatsapp.com/")
soup = bs4.BeautifulSoup(res.text , 'lxml')


browser = webdriver.Firefox()
browser.get("https://web.whatsapp.com/")
elm = browser.find_element_by_class_name('3j7s9')[0]
elm.click()

