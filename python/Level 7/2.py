from collections import deque
import string
class caesar():
    def __init__(self, test):
        lowere = deque(string.ascii_lowercase)
        lowerd = deque(string.ascii_lowercase)
        lowere.rotate(-test)
        lowerd.rotate(test)
        lowereall = ''.join(lowere)
        lowerdall = ''.join(lowerd)
        ###########
        uppere = deque(string.ascii_uppercase)
        upperd = deque(string.ascii_uppercase)
        uppere.rotate(-test)
        upperd.rotate(test)
        uppereall = ''.join(uppere)
        upperdall = ''.join(upperd)
        ###########
        self.alle = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, lowereall + uppereall)
        self.alld = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, lowerdall + upperdall)
    def encrypt(self, text):
        return text.translate(self.alle)

    def decrypt(self, text):
        return text.translate(self.alld)   
     
text = input("Enter your text: ")
key = input("Enter your key: ") 
try:
    if 0 < int(key) <= 26:  
        cipher = caesar(4)  
        enc = cipher.encrypt(text)
        dec = cipher.decrypt(enc)
        print(f"Original: {text}")
        print(f"Encrypted: {enc}")
        print(f"Decrypted: {dec}")
    else:
        print("Key must be between 1 and 26!")    
except:
    print("Error happened! make sure the key is integer")        