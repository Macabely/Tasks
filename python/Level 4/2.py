import re
def password():
    test = input("Please enter you password: ")
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', test):
        return("Your password is strong")
    else:

        return(f"Your password '{test}' is weak.\nPlease make sure the password containsat (at least 8 characters, includes a number, and a special character).")   

print(password())        