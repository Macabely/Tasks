import requests

url = 'https://httpbin.org/headers'
headers = {
    'User-Agent': 'Hello how are you, iam fine thank you :)',
    'Accept': 'accept ya3m ay 7aga',
    'Accept-Language': 'ay raz3',
    'Connection': 'keep-alive'
}

response = requests.get(url, headers=headers)
print(response.content.decode())