ports = {
        20: "FTP Data (credential sniffing, data exfiltration)",
        21: "FTP Control (brute-forcing, anonymous access)",
        22: "SSH (brute-forcing, key theft, tunneling)",
        23: "Telnet (plaintext sniffing, default creds)",
        25: "SMTP (email spoofing, user enumeration)",
        42: "WINS (NetBIOS spoofing, network enumeration)",
        49: "TACACS (weak encryption, credential theft)",
        53: "DNS (spoofing, tunneling, BIND exploits)",
        67: "DHCP (spoofing, DoS via lease exhaustion)",
        68: "DHCP (spoofing, DoS via lease exhaustion)",
        69: "TFTP (unauthenticated file access)",
        80: "HTTP (web exploits, SQL injection)",
        88: "Kerberos (Kerberoasting, Golden Ticket attacks)",
        110: "POP3 (credential theft, email exfiltration)",
        111: "RPCbind (NFS enumeration, RPC exploits)",
        123: "NTP (DDoS amplification, time exploits)",
        135: "MS RPC (EternalBlue, Windows exploits)",
        137: "NetBIOS (SMB enumeration, credential theft)",
        138: "NetBIOS (SMB enumeration, credential theft)",
        139: "NetBIOS (SMB enumeration, credential theft)",
        143: "IMAP (credential theft, email exfiltration)",
        161: "SNMP (community string brute-forcing)",
        389: "LDAP (user enumeration, privilege escalation)",
        443: "HTTPS (SSL misconfigs, web exploits, MITM)"
    }

t = True

while t:

    user = (input("Enter the port number: "))
    if user.isdigit():
        s = int(user)
        if s in ports:
            print("Port is common:",ports.get(s))
            t = False
        else:
            print("Not common")
    else:
        print("Please enter a number")        