import os
try:
    from zipfile import ZipFile
    path = input("Enter a file path: ")
    path2 = f"./test.zip"
    with ZipFile(path2, "w") as z:
        z.write(path)
        print("Your zip file locate at:",os.path.abspath(f"{path2}"))
except:
    print("Error occurred! Enter a valid path")