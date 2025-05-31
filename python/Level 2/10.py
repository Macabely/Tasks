test = input("Please enter your string: ")
if test == test[::-1]:
    print(test,"<==>",test[::-1])
    print("The string is a palindrome")
else:
    print(test,"<==>",test[::-1])
    print("The string is not a palindrome")