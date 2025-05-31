import random
import string
def generate():
    test = string.ascii_letters + string.digits + string.punctuation
    mac = "".join(random.choice(test) for i in range(12))
    return(f"Your generated password is: {mac}")

print(generate())