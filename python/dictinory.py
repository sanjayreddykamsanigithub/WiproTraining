Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> dict1={1:10,2:20,3:30}
>>> dict1
{1: 10, 2: 20, 3: 30}
>>> dict1[2]
20
>>> dict2={'a':10,'b':20,'c':30}
>>> dict2
{'a': 10, 'b': 20, 'c': 30}
>>> dict2['c']
30
>>> student={'rno':101,'name':'sanju','city':'jangoan'}
>>> student['name']
'sanju'
>>> student['city']='vriha'
>>> student
{'rno': 101, 'name': 'sanju', 'city': 'vriha'}
>>> student['fname']='veera'
>>> student
{'rno': 101, 'name': 'sanju', 'city': 'vriha', 'fname': 'veera'}
>>> student.get('name')
'sanju'
>>> student.keys()
dict_keys(['rno', 'name', 'city', 'fname'])
>>> student.values()
dict_values([101, 'sanju', 'vriha', 'veera'])
>>> student.pop('fname')
'veera'
>>> student
{'rno': 101, 'name': 'sanju', 'city': 'vriha'}
