text = input("Enter a string: ")
text = text.lower()
test = {}

for i in text:
    if i.isalpha():
        test[i] = test.get(i, 0) + 1

if test:
    print("Letter counts:")
    for letter, count in sorted(test.items()):
        print(f"'{letter}': {count}")
else:
    print("No letters found in the string.")