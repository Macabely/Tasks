def valid():
    user = input("Please enter your IP: ")
    test = user.split(".")
    if len(test) != 4:
        return ("IP is not valid! Please enter the right format (0.0.0.0 - 255.255.255.255)")
    for n in test:
        if n.isdigit() == False:
            return ("IP is not valid! Please enter an integer")
        if int(n) < 0 or int(n) > 255:
            return ("IP is not valid!")
    return(f"{user} is a valid IP")    
print(valid())