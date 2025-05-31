import os
user = input("Type any thing: ")
file = open(f"{user}", "w")
file.write(f"{user}")

file = open(os.path.abspath(user), "r")
print("Your file locate at:",os.path.abspath(f"{user}"))
print(file.read())