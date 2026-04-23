Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id(s1)
2241275770560
s2='hi'
id(s2)
140733987763640
s3=s1
id(s3)
2241275770560
s3
'hello'
s1
'hello'
s1='hi'
id9s1)
SyntaxError: unmatched ')'
id(s1)
140733987763640
s1='india'
id(s1)
2241304991552
list1=[10,20,30,40,50]
list1
[10, 20, 30, 40, 50]
type(list1)
<class 'list'>
list[0]
list[0]
list[-1]
list[-1]
list1[-1]
50
list1[0]
10
list1[0:3]
[10, 20, 30]
list1[0:3:2]
[10, 30]
list2=list('hi','hello')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list2=list('hi','hello')
TypeError: list expected at most 1 argument, got 2
s1
'india'
list2=list(s1)
list2
['i', 'n', 'd', 'i', 'a']
list3=liist1
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    list3=liist1
NameError: name 'liist1' is not defined. Did you mean: 'list1'?
list3=list1
list3
[10, 20, 30, 40, 50]
id(list1)
2241303948160
id(list3)
2241303948160
list4=[100,'hi',100,True,69.36]
list4[5]='hey'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    list4[5]='hey'
IndexError: list assignment index out of range
list1.append('hey')
list1
[10, 20, 30, 40, 50, 'hey']
list1.remove('hey')
list1
[10, 20, 30, 40, 50]
list4.append(2000)
list4
[100, 'hi', 100, True, 69.36, 2000]
list4.remove(20000)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list4.remove(20000)
ValueError: list.remove(x): x not in list
list4.count(23)
0
list4.count(100)
2
list1.insert(2,100)
list1
[10, 20, 100, 30, 40, 50]
id(list1)
2241303948160
list1.pop()
50
list1
[10, 20, 100, 30, 40]
list1.pop(2)
100
list1
[10, 20, 30, 40]
list2
['i', 'n', 'd', 'i', 'a']
list2.clear()
list2
[]
id(list2)
2241305030464
del(list2)
list2
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list2
NameError: name 'list2' is not defined. Did you mean: 'list1'?
id(list2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    id(list2)
NameError: name 'list2' is not defined. Did you mean: 'list1'?
list2=list1
list1
[10, 20, 30, 40]
list2
[10, 20, 30, 40]
id(list1)
2241303948160
id(list2)
2241303948160
list1[1]=200
list1
[10, 200, 30, 40]
ist2
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    ist2
NameError: name 'ist2' is not defined. Did you mean: 'list2'?
list2
[10, 200, 30, 40]
list2=list(list1)
list1
[10, 200, 30, 40]
list2
[10, 200, 30, 40]
id(list1)
2241303948160
id(list2)
2241305029184
list[1]=20
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    list[1]=20
TypeError: 'type' object does not support item assignment
list1[1]=20
list1
[10, 20, 30, 40]
list2
[10, 200, 30, 40]
tuple1=(11,22,33,44,55)
tuple1
(11, 22, 33, 44, 55)
tuple1[3]
44
tuple1[30]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    tuple1[30]
IndexError: tuple index out of range
tuple1[0:4:2]
(11, 33)
tuple1.index(44))
SyntaxError: unmatched ')'
tuple1.index(44)
3
tuple1.count(22)
1
tuple2=tuple1
tuple2
(11, 22, 33, 44, 55)
tuple3=tuple(list1)
tuple3
(10, 20, 30, 40)
list1
[10, 20, 30, 40]
list1.append(tuple1)
list1
[10, 20, 30, 40, (11, 22, 33, 44, 55)]
list1[0]
10
list1[2]
30
list1[3]
40
list1[4]
(11, 22, 33, 44, 55)
list5=list(tuple1)
list5
[11, 22, 33, 44, 55]
list1[3:1]
[]
list1[3][2]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    list1[3][2]
TypeError: 'int' object is not subscriptable
>>> list1[3][2]
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    list1[3][2]
TypeError: 'int' object is not subscriptable
>>> set1={10,20,30,40,50}
>>> set1
{50, 20, 40, 10, 30}
>>> set1.add(25)
>>> set1
{50, 20, 40, 25, 10, 30}
>>> set1.add('25')
>>> set1
{50, 20, 40, 25, 10, '25', 30}
>>> set1.add(25)
>>> set1
{50, 20, 40, 25, 10, '25', 30}
>>> set2=set(set1)
>>> set2
{50, 20, 40, 25, 10, '25', 30}
>>> set2.remove('25')
>>> set2
{50, 20, 40, 25, 10, 30}
>>> set1
{50, 20, 40, 25, 10, '25', 30}
>>> set1.union(set2)
{40, '25', 10, 50, 20, 25, 30}
>>> set1.intersection(set2)
{40, 10, 50, 20, 25, 30}
