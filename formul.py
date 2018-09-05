#!/usr/bin/env  python2

import  sys
import time

#  taking all numbers to multiply 
user_data=sys.argv[1:]

mul=1

#iteration for checking all inputs one by one and multiply them all
for   i   in  user_data:
	mul=mul*int(i)


print  "multiplication of all given numbers is:  ",mul

