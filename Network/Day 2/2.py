i = input("Enter your port number: ")
if int(i) in range (0, 65536):
    print("Port is valid")
else:
    print("Port not valid")
