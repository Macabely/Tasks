username = "admin"
password = "testing"
now = 0

while now < 3:
    input_username = input("Please enter your username: ")
    input_password = input("Please enter your password: ")
    if input_username == username and input_password == password:
        print(f"Hello {input_username} you are logged in")
        break
    else:
        now += 1
        remain = 3 - now
        if remain == 1:
            print(f"Wrong credentials! you have {remain} time left.")
        elif remain == 0:
            continue    
        else:    
            print(f"Wrong credentials! you have {remain} times left.")

if now == 3:
    print("Too many attempts, you have reached your limits.")        