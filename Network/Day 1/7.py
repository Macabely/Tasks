import subprocess
import os
def ping_ip(ip):

    cmd = ["ping", "-n", "1", ip] if os.name == "nt" else ["ping", "-c", "1", ip]
    result = subprocess.run(cmd, stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL)
    return "ip is reachable" if result.returncode == 0 else "ip unreachable"

print(ping_ip("8.8.8.8"))