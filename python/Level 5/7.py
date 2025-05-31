import os
try:
    path = input("Enter the path of the folder u wanna delete files from: ")
    files = os.listdir(path)
    for file in files:
        test = os.path.join(path, file)
        if os.path.isfile(test):
            os.remove(test)
    print("Files deleted.")
except:
    print("Error occurred while deleting! Enter a valid path")        
