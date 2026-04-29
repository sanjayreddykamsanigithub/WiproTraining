import re
# beg & end pattern
'''txt = input('Enter a text')
bpat = input('Enter beginning pattern')
epat = input('Enter ending pattern')
bpat = '^' + bpat
epat = epat + '$'

if re.search(pattern=bpat,string=txt):
    print('Beginning pat available')
else:
    print('Beginning pat not available')

if re.search(pattern=epat,string=txt):
    print('Ending pat available')
else:
    print('Ending pat not available')'''

#digit
'''txt = input('Enter a text')
mbno = input('Enter a text')
pat = r"\d"

if re.fullmatch(pattern=pat, string=mbno):
    print('Only digits')
else:
    print('Only digits')'''


'''un = input('Enter UN')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')'''

#email

'''emailadd = input('Email')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=emailadd):
    print('Valid')
else:
    print('Invalid')'''

#pwd
'''pwdtxt = input('pwd : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"

if re.match(pattern=pat, string=pwdtxt):
    print('Valid')
else:
    print('Invalid')'''

txt = input('Text ')
pat = r"\s+"

print(re.split(pattern=pat, string=txt))

