
'''#nat nos print
num = int(input('Enter a number'))

sum = 0
for i in range(1, num):
    sum = sum + i**2
print('Sum of squares of natural numbers : ', sum)
'''

#print * for n times
num = int(input('Enter a number'))

for _  in  range(1, num+1):
    print('*', '&', sep=' ',end='\t')