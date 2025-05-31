import os

dir_path = input("Enter the directory path: ")
word = input("Enter the word that you want to search for: ")

try:
    for root, _, files in os.walk(dir_path):
        for file in files:
            cur_path = os.path.join(root, file)
            try:
                with open(cur_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if word in content:
                        print(f'String "{word}" found in "{os.path.abspath(cur_path)}"')
                        break
            except (UnicodeDecodeError, PermissionError, OSError):
                continue
        else:
            continue  # Skip to next subdirectory if no match in current one
        break  # Break outer loop if match found
    else:
        print(f'String "{word}" not found in any file.')
except (FileNotFoundError, PermissionError):
    print("Error: The directory path is invalid or inaccessible.")