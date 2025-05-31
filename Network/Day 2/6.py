def test():
    try:
        t = input("Enter the port number: ")
        if int(t) in range(0, 1024):
            return "Port in privileged range"
        else:
            return "Port not in privileged range"
    except ValueError:
        return "Invalid port! port must be between 0 - 65535"
print(test())          
 