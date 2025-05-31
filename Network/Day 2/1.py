ports = {
    80 : "HTTP",
    443 : "HTTPS",
    3306 : "MySQL",
    22 : "SSH",
    21 : "FTP",
    23 : "Telnet",
    53 : "DNS",
    587 : "SMTP",
}
t = True

while t:

    user = (input("Please enter the port number: "))
    if user.isdigit():
        test = int(user)
        if test in ports:
            print(ports.get(test))
            t = False
        else:
            print("Out of range")
    else:
        print("Please enter a number")