names = {
    "Ahmed" : 1234,
    "Mohamed" : "test123",
    "Ali" : "SuperAdmin",
    "Test" : "best"
}

for name in names:
    name = input("Please enter you username: ").capitalize()
    if name in names:
        print(f"Hello {name}. \nYour password is: {names[name]} ")
        break
    else:
        print("Wrong name! Please enter you username again: ")