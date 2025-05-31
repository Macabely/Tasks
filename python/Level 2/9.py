password = "admin"
test = True
while test:
    input_password = input("Please enter your password: ")

    if input_password == password:
        print("The password is correct")
        test = False
    else:
        print("Wrong password, please try again")