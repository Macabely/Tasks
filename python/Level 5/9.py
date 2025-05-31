import os
dir = input("Enter the directory path: ")
largest_size = -1
largest_file = ""

for root, _, files in os.walk(dir):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        if size > largest_size:
            largest_size = size
            largest_file = file_path
if largest_size >= 0:
    print(f"Largest file: {largest_file} ({largest_size} bytes)")
else:
    print("No files found in the directory.")
