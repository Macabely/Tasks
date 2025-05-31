import requests
ip = requests.get("https://api.ipify.org").content.decode('utf8')
print(f"My ip is: {ip}")