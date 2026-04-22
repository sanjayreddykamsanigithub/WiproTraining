text = "abracadabra"
count = 0

for index, char in enumerate(text):
    if char == 'a':
        count += 1

print("Number of 'a' in string:", count)