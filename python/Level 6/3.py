import requests
url = "https://example.com"
res = requests.post(url)
for header, value in res.headers.items():
    print(f"{header}: {value}")