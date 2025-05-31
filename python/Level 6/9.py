import subprocess
import os
ip_list = ["192.168.1.1", "192.168.1.100", "8.8.8.8", "10.0.0.1"]

def ping_ip(ip):
    cmd = ["ping", "-n", "1", ip] if os.name == "nt" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return "live" if result.returncode == 0 else "down"

def main():
    print("Pinging IPs and checking status...\n")
    for ip in ip_list:
        status = ping_ip(ip)
        print(f"{ip}: {status}")

if __name__ == "__main__":
    main()