import os
user = input("Type any thing: ")
file = open("keystroke.log", "a")
file.write(f"{user}\n")
print("The logs locate at:",os.path.abspath("keystroke.log"))