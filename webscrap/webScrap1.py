#!/usr/bin/python

import sys
import time
import requests
import bs4

a='+'
print " "
#for inline input 
user=sys.argv
x,y=user[1:3]

print "waiting for swapping the inputs..."
print " "
time.sleep(2);

#swapping inputs
x,y=y,x

print "inputs has been swapped!!!"
print " "
print "x is:",x
print "y is:",y
print " "

#webscrapping

print "searching web for ",x," ",y
print " "
time.sleep(2)

print "scrapping 10 result we got from web....."
print " "
time.sleep(2)
res = requests.get('https://www.google.co.in/search?q='+x+a+y)
soup = bs4.BeautifulSoup(res.text, 'lxml')
a = soup.select('.r')
b = soup.select('.hJND5c')
print "data scrapped"
print " "
time.sleep(1)
print("here is the data:")
print " "
i=0
while(i<10):
	print(a[i].text)
	print " "
	print "     ", b[i].text
	print " "
	time.sleep(1)
	i=i+1


