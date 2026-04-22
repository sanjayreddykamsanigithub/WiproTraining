Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hEllO'
s1.casefold()
'hello'
s1='HeLLo'
s1.casefold()
'hello'
s1.count('l')
0
s1.find('L')
2
s1.join('sanju')
'sHeLLoaHeLLonHeLLojHeLLou'
s1.isidentifier('H')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1.isidentifier('H')
TypeError: str.isidentifier() takes no arguments (1 given)
s1.isidentifier()
True
s1.replace('H','S')
'SeLLo'
s1.split('')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s1.split('')
ValueError: empty separator
s1.split()
['HeLLo']
s1[0]
'H'
s1[-2]
'L'
s1[0:3]
'HeL'
>>> s1[0:4:2]
'HL'
>>> s1[::2]
'HLo'
>>> s1="Hello sanjay welcome to wipro!"
>>> s1[-10::-2]
' mce ansolH'
>>> s1[-8::4]
'op'
>>> s1[::3]
'Hlsj lmtwr'
>>> 
================== RESTART: C:/Wipro Trainee/python/str1ex.py ==================
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
>>> 
================== RESTART: C:/Wipro Trainee/python/str1ex.py ==================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
