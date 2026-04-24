**QUESTION 1:**



Do the following in a single program using built-in functions 

Take a list of numbers as input and print the largest and smallest numbers in the list. 

Take a string as input and print the length of the string. 

Take a list of names as input and print the list in alphabetical order. 

Take a list of numbers as input and print the total sum of the elements in the list. 

Takes a string as input and print the string in uppercase.



**SINGLE PROGRAM:**



numbers = \[10, 5, 20, 3, 8]

print("Largest number:", max(numbers))

print("Smallest number:", min(numbers))



text = "python"

print("Length of string:", len(text))



names = \["john", "Alice", "Bob"]

names.sort()

print("Sorted names:", names)



print("Sum of numbers:", sum(numbers))



print("Uppercase string:", text.upper())



**OUTPUT:**



Largest number: 20

Smallest number: 3

Length of string: 6

Sorted names: \['Alice', 'Bob', 'john']

Sum of numbers: 46

Uppercase string: PYTHON

\----------------------------------------



**QUESTION 2:**



Write a user-defined function factorial(n) that takes a positive integer n as an argument 

and returns its factorial. Use the function in a program and print the factorial of a given 

number. 



**PROGRAM:**



def factorial(n):

&#x20;   result = 1

&#x20;   for i in range(1, n + 1):

&#x20;       result \*= i

&#x20;   return result



num = 6

print("Factorial of", num, "is:", factorial(num))



**OUTPUT:**



Factorial of 6 is: 720

\-------------------------------------------------



**QUESTION 3:**



Write a user-defined function "find\_largest(a, b, c)" that takes three numbers as 

arguments and returns the largest of the three. Use the function in a program to find and 

print the largest of three given numbers.



**PROGRAM:**



def find\_largest(a, b, c):

&#x20;   return max(a, b, c)



print("largest number:", find\_largest(10, 25, 15))



**OUTPUT:**



largest number: 25

\--------------------------------------------------



**QUESTION 4:**



Write a user-defined function greet(name) that takes a name as an argument and prints 

a greeting message like "Hello, \[name]!" Use the function to greet the user with their 

name. 



**PROGRAM:**



def greet(name):

&#x20;   print("Hello,", name + "!")



greet("Sanjay")



**OUTPUT:**



Hello, Sanjay!

\--------------------------------------------



**QUESTION 5:**



Combining Built-in and User-Defined Functions: 

Find the Average of a List: 

Write a user-defined function average(numbers) that takes a list of numbers as an 

argument and returns the average of the numbers. Call the function with a list of 

numbers and print the average. 



**PROGRAM:**



def average(numbers):

&#x20;   return sum(numbers) / len(numbers)



nums = \[10, 20, 30, 40, 50]

print("Average:", average(nums))



**OUTPUT:**



Average: 30.0

\--------------------------------------



**QUESTION 6:**



Check Palindrome: 

Write a user-defined function is\_palindrome(s) that takes a string as an argument and 

returns True if the string is a palindrome (reads the same forward and backward), and 

False otherwise. Test the function with different strings and print the results. 



**PROGRAM:**



def is\_palindrome(s):

&#x20;   return s == s\[::-1]



print("madam:", is\_palindrome("madam"))

print("hello:", is\_palindrome("hello"))



**OUTPUT:**



madam: True

hello: False

\---------------------------------------



**QUESTION 7:**



Use the Math Module: 

Write a program that imports the math module and uses it to: 

Find the square root of a number. 

Calculate the sine of an angle . 

Find the greatest common divisor (GCD) of two numbers .



**PROGRAM:**



import math

num = 25

print("Square root:", math.sqrt(num))



angle = math.radians(30)

print("Sin of 30 degrees:", math.sin(angle))



print("GCD:", math.gcd(12, 18))



**OUTPUT:**



Square root: 5.0

Sin of 30 degrees: 0.49999999999999994

GCD: 6

\-------------------------------------------



**QUESTION 8:**



Use the Random Module: 

Write a program that imports the random module and uses it to: 

Generate and print a random integer between 1 and 100. 

Create a list of random numbers  and print the list. 

Shuffle a list of numbers and print the shuffled list.



**PROGRAM:**



import random

print("Random number:", random.randint(1, 100))



random\_list = \[random.randint(1, 100) for \_ in range(5)]

print("Random list:", random\_list)



random.shuffle(random\_list)

print("Shuffled list:", random\_list)



**OUTPUT:**



Random number: 18

Random list: \[31, 74, 71, 13, 78]

Shuffled list: \[13, 71, 74, 78, 31]

\-------------------------------------------



**QUESTION 9:**



Use the Datetime Module: 

Write a program that imports the datetime module and uses it to: 

Get and print the current date and time . 

Calculate and print the number of days between two dates. 

Format and print the current date in the format "DD-MM-YYYY" 



**PROGRAM:**



from datetime import datetime



now = datetime.now()

print("Current Date and Time:", now)



date1 = datetime(2024, 1, 1)

date2 = datetime(2024, 1, 10)



difference = date2 - date1

print("Number of days between dates:", difference.days)



formatted\_date = now.strftime("%d-%m-%Y")

print("Formatted Date:", formatted\_date)



**OUTPUT:**



Current Date and Time: 2026-04-24 23:49:36.256756

Number of days between dates: 9

Formatted Date: 24-04-2026

\--------------------------------------------------



**QUESTION 10:**



Use the OS Module: 

Write a program that imports the os module and uses it to: 

Print the current working directory  

Create a new directory and verify its existence. 

List all files and directories in the current directory



**PROGRAM:**



import os

cwd = os.getcwd()

print("Current Working Directory:",  cwd)



folder\_name = "test\_folder"

if not os.path.exists(folder\_name):

&#x20;   os.mkdir(folder\_name)

&#x20;   print("Folder created:", folder\_name)

else:

&#x20;   print("Folder already exists:", folder\_name)



print("Does folder exist?", os.path.exists(folder\_name))

print("\\nFiles and directories:")

for item in os.listdir():

&#x20;   print(item)



**OUTPUT:**



Current Working Directory: C:\\Wipro Trainee\\PythonProject\\daily\_assignments

Folder already exists: test\_folder

Does folder exist? True



Files and directories:

average\_main.py

built\_in\_main.py

count a

count a.py

count a.txt

datetime\_main.py

day 3 assignment.txt

factorial\_main.py

greet\_main.py

largest\_main.py

math\_main.py

math\_module\_main.py

my\_math

os\_main.py

palindrome\_main.py

random\_module\_main.py

string\_main.py

string\_utils

sum of numbers

sum of numbers.py

sum of numbers.txt

test\_folder

\--------------------------------------------



**QUESTION 11:**



Create and Use a Custom Package: 

Create a package called my\_math with two modules: arithmetic.py and geometry.py. 

In arithmetic.py, define functions for addition, subtraction, multiplication, and division. 

In geometry.py, define functions to calculate the area of a circle and the area of a 

rectangle. 

Write a program that imports these functions from the my\_math package and uses 

them to perform various calculations.



**PROGRAM:**



**my\_math.py -> arithmetic.py**



def add(a, b):

&#x20;   return a + b



def subtract(a, b):

&#x20;   return a - b



def multiply(a, b):

&#x20;   return a \* b



def divide(a, b):

&#x20;   if b == 0:

&#x20;       return "Cannot divide by zero"

&#x20;   return a / b



**my\_math(python package) -> geometry.py**



import math



def area\_circle(radius):

&#x20;   return math.pi \* radius \* radius



def area\_rectangle(length, width):

&#x20;   return length \* width



**math\_main.py file**



from my\_math.arithmetic import add, subtract, multiply, divide

from my\_math.geometry import area\_circle, area\_rectangle



print("Addition:", add(10, 5))

print("Subtraction:", subtract(10, 5))

print("Multiplication:", multiply(10, 5))

print("Division:", divide(10, 5))



**OUTPUT:**



Addition: 15

Subtraction: 5

Multiplication: 50

Division: 2.0

Area of Circle: 78.53981633974483

Area of Rectangle: 24

\---------------------------------------------------



**QUESTION 12:**



Create a Package for String Utilities: 

Create a package called string\_utils with two modules: string\_operations.py and 

string\_validations.py. 

In string\_operations.py, define functions for reversing a string, converting a string to 

uppercase, and finding the length of a string. 

In string\_validations.py, define functions to check if a string is a palindrome and if it 

contains only alphabetic characters. 

Write a program that imports and uses these functions from the string\_utils package.



**PROGRAM:**



**daily\_assignments(directory) -> string\_utils(python package)**



def reverse\_string(s):

&#x20;   return s\[::-1]



def to\_uppercase(s):

&#x20;   return s.upper()



def string\_length(s):

&#x20;   return len(s)



**string\_validations.py**



def is\_palindrome(s):

&#x20;   return s == s\[::-1]



def is\_alphabetic(s):

&#x20;   return s.isalpha()



**string\_main.py**



from string\_utils.string\_operations import reverse\_string, to\_uppercase, string\_length

from string\_utils.string\_operations import reverse\_string, to\_uppercase, string\_length

from string\_utils.string\_validations import is\_palindrome, is\_alphabetic



text = "madam"



print("Reversed:", reverse\_string(text))

print("Uppercase:", to\_uppercase(text))

print("Length:", string\_length(text))



print("Is Palindrome:", is\_palindrome(text))

print("Is Alphabetic:", is\_alphabetic(text))



**OUTPUT:**



Reversed: madam

Uppercase: MADAM

Length: 5

Is Palindrome: True

Is Alphabetic: True

\------------------------------------------------













