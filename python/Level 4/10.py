def test():
    user = str(input("Enter your string: "))
    vowels = "aeiouAEIOU"
    a = [char for char in user if char in vowels]
    if user.isdigit() == True:
        return "Error! Please enter a string"
    "".join(a)

    return f"Your string '{user}' has {a} vowels."    

print(test())