import os
try:
    user = input("Enter the absloute path of a folder that contains files: ")
    dir = rf"{user}"
    List = []
    
    for file in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, file)):
            List.append(file)
    if len(List) == 0:
        print("Empty folder! Make sure the folder contains files")
    else:    
        print(List)        
except:
    print("Enter a valid absloute path")    