message = input("Enter you massage: ")
key = "key"

def xor(message, key):
# make sure key matches the message length
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    # encrypt each character in the message with the corresponding key character
    result = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))
    return result

encrypted = xor(message, key)
print(f"Encrypted message ==> {encrypted}")