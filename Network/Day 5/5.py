import requests
url = "https://my.te.eg/"
try:
    if not url.endswith("/"):
        url += "/"
    robots = url + "robots.txt"        
    res = requests.get(robots)
    if res.status_code == 200:
        print(res.text)
    else:
        print("No robots.txt found")
except Exception as e:
    print(f"Error {e}")
