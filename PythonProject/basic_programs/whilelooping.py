
'''
#natural numbers printing

num = int(input('Enter a number'))
value = 1

while value <= num:
    print(value)
    value = value + 1
'''

num = input('Enter a number')

count = len(num)
sum = 0
ni = int(num)
comp = ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni // 10

if comp == sum:
    print('Armstrong')
else:
    print('Not an Armstrong')




