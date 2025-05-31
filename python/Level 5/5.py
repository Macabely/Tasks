import os
try:
    folder = input("Please enter the folder path: ")

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            old = os.path.join(folder, file)
            new = file[:-4] + ".bak"
            test = os.path.join(folder, new)
            os.rename(old, test)
            print(f"Renamed: {file} -> {new}")

    print("Files have been renamed to .bak")
except:
    print("Error! no files exist in this path.")