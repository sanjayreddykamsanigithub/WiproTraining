'''#ARBITARY
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum'''

'''numbers = list()
count = int(input('How many ? '))
for _ in range(1, count+1):
    numbers.append(int(input('No: ')))'''

'''#ARBITARY
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

print(add( 5,6,9))
print(add(  5,6,))
print(add(  5,6,9,3,10,8,7,23))'''

'''def add(n1, n2, n3=10):
    return n1 + n2 + n3

num1=int(input('Enter a number'))
num2=int(input('Enter another number'))

print(add(num1, num2))
print(add(num1, num2, 100))'''

'''#lambda

num1=int(input('Enter a number'))
num2=int(input('Enter another number'))

add = lambda n1, n2 : n1+n2

print(add(num1, num2))'''

numbers = [1,2,3,4,5]

'''sq = lambda nums : (num * num for num in nums )
print(tuple( sq(numbers) ))'''

sq = lambda nums : [num * num for num in nums if num%2==0 ]
print(sq(numbers) )
