from scapy.all import IP, TCP, sr1
import sys
import ipaddress

def validates(ip, port):
    try:
        ipaddress.ip_address(ip) 
        if not 0 <= port <= 65535:
            raise ValueError("Port must be between 0 and 65535")
        return True
    except ValueError as e:
        print(f"Invalid input: {e}")
        return False

def inject(target_ip, target_port):
    try:
        ip = IP(dst=target_ip)
        tcp = TCP(sport=12345, dport=target_port, flags="S", seq=1000)
        packet = ip / tcp
        
        print(f"Sending SYN packet to {target_ip}:{target_port}")
        response = sr1(packet, timeout=2, verbose=False)
        
        if response:
            if response.haslayer(TCP):
                tcp_flags = response.getlayer(TCP).flags
                if tcp_flags == 0x12:  
                    print(f"Port {target_port} is open >--SYN-ACK received--<.")
                elif tcp_flags == 0x14: 
                    print(f"Port {target_port} is closed >--RST-ACK received--<.")
                else:
                    print(f"Unexpected TCP flags: {hex(tcp_flags)}")
            else:
                print("Non-TCP response received.")
        else:
            print(f"No response from {target_ip}:{target_port}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    target_ip = input("Enter target IP: ")
    try:
        target_port = int(input("Enter target port: "))
    except ValueError:
        print("Port must be a number.")
        return
    
    if not validates(target_ip, target_port):
        return
    
    inject(target_ip, target_port)

if __name__ == "__main__":
    main()