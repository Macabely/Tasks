import re

test = input("Enter the file path: ")
regex = re.compile(r'[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})*')
l = []

with open(test, 'r') as e:
    for line in e:
        match = regex.findall(line)
        l.extend(match)
e.close()
print(l)        