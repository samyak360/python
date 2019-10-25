Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=1
>>> b=2
>>> a
1
>>> b
2
>>> "a{}  b{}".format(a,b)
'a1  b2'
>>> a={"b":12,}
'
>>> a={"b":12,"c":23}
>>> a
{'b': 12, 'c': 23}
>>> "aa={b}  as={c}".format(**a)
'aa=12  as=23'
>>> t=[123,345]
>>> t
[123, 345]
>>> u={347,456)
SyntaxError: invalid syntax
>>> 
>>> u=(347,456)
>>> u
(347, 456)
>>> compl=12+3j
>>> cpmpl.real
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    cpmpl.real
NameError: name 'cpmpl' is not defined
>>> compl
(12+3j)
>>> compl.real
12.0
>>> compl.imag
3.0
>>> a=10
>>> "dec {0:d} bin{0:b} hex{0:x}.format(a)
SyntaxError: EOL while scanning string literal
>>> "dec {0:d} bin{0:b} hex{0:x}".format(a)
'dec 10 bin1010 hexa'
>>> "dec {0:#d} bin{0:#b} hex{0:#x}".format(a)
'dec 10 bin0b1010 hex0xa'
>>> "(:,)".format(19238711321)
'(:,)'
>>> "{:,}".format(19238711321)
'19,238,711,321'
>>> "{:.}".format(19238711321)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    "{:.}".format(19238711321)
ValueError: Format specifier missing precision
>>> "{:>20}".format(19 23871 1321)
SyntaxError: invalid syntax
>>> "{:>20}".format(ljasd askjdhad ashdj)
SyntaxError: invalid syntax
>>> "{:>20}".format(ljasdaskjdhad ashdj)
SyntaxError: invalid syntax
>>> "{:>20}".format{ljasdaskjdhad ashdj}
SyntaxError: invalid syntax
>>> "{:>20}".format("ljasdaskjdhad ashdj")
' ljasdaskjdhad ashdj'
>>> import datetime
>>> d=datetime.datetime(2019,12,12,3,2,4)
>>> d
datetime.datetime(2019, 12, 12, 3, 2, 4)
>>> "{:%Y %m %d %h %m %s}".format(d)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    "{:%Y %m %d %h %m %s}".format(d)
ValueError: Invalid format string
>>> "{:%Y-%m-%d %h:%m:%s:}".format(d)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    "{:%Y-%m-%d %h:%m:%s:}".format(d)
ValueError: Invalid format string
>>> "{:%Y-%m-%d %h:%m:%s}".format(d)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    "{:%Y-%m-%d %h:%m:%s}".format(d)
ValueError: Invalid format string
>>> min ("iI")
'I'
>>> min ("AaiI")
'A'
>>> "{:%Y-%M-%D %h:%m:%S}".format(d)
'2019-02-12/12/19 Dec:12:04'
>>> "{:%Y-%M-%D %H:%m:%S}".format(d)
'2019-02-12/12/19 03:12:04'
>>> "{:%Y-%M-%d %H:%m:%S}".format(d)
'2019-02-12 03:12:04'
>>> '2019-02-12 0"dec {0:d} bin{0:b} hex{0:x}.format(a)
SyntaxError: EOL while scanning string literal
>>> 
>>> lst={}
>>> lst
{}
>>> type(lst)
<class 'dict'>
>>> lst=()
>>> type(lst)
<class 'tuple'>
>>> lst=[]
>>> type(lst)
<class 'list'>
>>> for i in "qwerty":
	print(j,end:'-')
	
SyntaxError: invalid syntax
>>> for i in "qwerty":
	print(j,end='-')

	
Traceback (most recent call last):
  File "<pyshell#56>", line 2, in <module>
    print(j,end='-')
NameError: name 'j' is not defined
>>> for i in "qwerty":
	print(i,end='-')

	
q-w-e-r-t-y-
>>> for i in "qwerty":
	print(i,sep='-')

	
q
w
e
r
t
y
>>> for i in "qwerty":
	print(i,sep='--')

	
q
w
e
r
t
y
>>> lst=[1,2,3,[4,5,6],7,[8,9]]
>>> lst
[1, 2, 3, [4, 5, 6], 7, [8, 9]]
>>> for i in lst:
	print (i)

	
1
2
3
[4, 5, 6]
7
[8, 9]
>>> print(lst[3])
[4, 5, 6]
>>> for i in lst:
	for j in i:
		print (j)

		
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    for j in i:
TypeError: 'int' object is not iterable
>>> for i in lst:
	print (i,sep='-')

	
1
2
3
[4, 5, 6]
7
[8, 9]

>>> "{}".format(lst)
'[1, 2, 3, [4, 5, 6], 7, [8, 9]]'
>>> for i in lst:
	if type(i)==list:
	for j in i:
		print (j)
		
SyntaxError: expected an indented block
>>> for i in lst:
	if type(i)==list:
	for j in i:
		print (j)
		
SyntaxError: expected an indented block
>>> for i in lst:
	if type(i)==list:
	for j in i:
		print (j)
		
SyntaxError: expected an indented block
>>> for i in lst:
	if type(i)==list:
	for j in i:
		print (j);
		
SyntaxError: expected an indented block
>>> for i in lst:
	if type(i)==list:
	for j in i:
		print (j)
		
SyntaxError: expected an indented block
>>> for i in lst:
	if type(i)==list:
		for j in i:
			print (j)
	else:
		print(i)

		
1
2
3
4
5
6
7
8
9
>>> from collections.abc import iterable
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    from collections.abc import iterable
ImportError: cannot import name 'iterable' from 'collections.abc' (H:\python\lib\collections\abc.py)
>>> from collections.abc import Iterable
>>> lst
[1, 2, 3, [4, 5, 6], 7, [8, 9]]
>>> for i in lst:
	if (isinstance(i,Iterable)):
		for j in i:
			print (j)
	else:
		print(i)

		
1
2
3
4
5
6
7
8
9
>>> 
>>> lst
[1, 2, 3, [4, 5, 6], 7, [8, 9]]
>>> lst.copy(lst1)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    lst.copy(lst1)
NameError: name 'lst1' is not defined
>>> lst1.copy(lst)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    lst1.copy(lst)
NameError: name 'lst1' is not defined
>>> lst1[]
SyntaxError: invalid syntax
>>> lst1=[2]
>>> lst1.copy(lst)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    lst1.copy(lst)
TypeError: copy() takes no arguments (1 given)
>>> ls=["abc", "abcd", "abcde"]
>>> ls
['abc', 'abcd', 'abcde']
>>> for i in ls:
	if (len(i)==4):
		print (i.upper())

		
ABCD
>>> for i in ls:
	if (len(i)==4):
		print (i.upper())
	else:
		continue

	
ABCD
>>> ls=["abc", "abcd", "abcde"]
>>> for i in ls:
	if (len(i)==4):
		ls.append(i)
		
	print (ls)

	
['abc', 'abcd', 'abcde', 'abcd']
