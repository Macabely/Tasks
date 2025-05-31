try:

    number = int(input("Please enter a number: "))
    if number % 2 == 0 :
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
except:
    print("Please enter an integer")