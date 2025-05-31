password = "password = P@ssw0rd"
vowels = "aeiouAEIOU"
result = "".join("*" if i in vowels else i for i in password)

print(result)