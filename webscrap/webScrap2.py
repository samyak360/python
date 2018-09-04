#!/usr/bin/python

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

a='+'
print " "
#for inline input 
user=sys.argv
x,y=user[1:3]

print "opening firefox to search images of ",x,y

browser = webdriver.Firefox()
browser.get("https://www.google.co.in/search?q="+x+a+y)
elm = browser.find_element_by_link_text('Images')
elm.click()
