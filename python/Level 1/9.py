text = "H4ck3r"
result = ""
for i in range(len(text)):
    if i in [0, 3]:
        result += text[i].lower()
    else:
        result += text[i].upper()
print(result)