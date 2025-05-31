import hashlib
user = input("Please enter your string: ")
test = hashlib.md5()
test.update(user.encode("utf-8"))
print(test.hexdigest())
