try:
    user = input("Please enter the absloute path of the file: ")
    file = open(user)
    print(file.read())
except:
    print("File Not Foud! Please enter the absloute path")