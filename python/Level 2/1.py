test = "s3cr3t"

# if password == test:
#     print("Congratulations you are logged in.")
#     pass
# else:
#     print("Wrong password")        

while True:    
    password = input ("Please enter your password: ")
    if password == test:
        print("Congratulations you are logged in.")
        break
    else:
        print("Worng password")
        print("Enter your password again")