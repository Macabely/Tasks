import requests
url = ("https://www.google.com")
request = requests.get(url)
response = request.status_code
if response in range(200,300):
    print("Website is up")
elif response in range(300, 400):
    print("Website is redirected to somewhere else")
elif response in range(400, 500):
    print("Website is restricted! you don't have access")
else:
    print("Website is down")        