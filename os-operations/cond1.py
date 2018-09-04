#!/usr/bin/env  python2
import os

choice='''
Press  1  to  check your current MAC  address  : 
Press  2  to  check total amount to RAM and  CPU   :   
Press  3  to  check your current OS type and OS name  :
Press  4  to check your internet connection   :  
Press  5  to  close your internet connection if it is running  : 
Press  6  to  check your current date and time  :
Press  7  to  logout your system   :  
Press  8  to  Turn off everyone's internet in your current network  : 
'''

print choice 
x=int(raw_input())

if  x ==  1 : 
	os.system("ifconfig | grep ether")

elif x==2 :
	print "total ram is:"
        os.system("cat /proc/meminfo | grep MemTotal")
	print " "
	print "total no of cpu cores is:"
	os.system("cat /proc/cpuinfo | grep processor | wc -l")


elif x==3 :
	print "OS type is:"
	os.system("cat /etc/lsb-release | grep ID")
	print " "
	print "OS name or version is:"
	os.system("cat /etc/lsb-release | grep RELEASE")

'''
elif x==4 :


elif x==5 :


elif x==6 :


elif x==7 :


elif x==8 :


else :
	print "please choose from above"
'''
