import requests
from bs4 import BeautifulSoup

try:
    url = input("Enter a url: ")
    agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124'}

    response = requests.get(url, headers=agent)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all(['h1', 'h2', 'h3'])
    if tags:
        for i, tag in enumerate(tags, 1):
            if tag:
                print(f"{i}- {tag.text}")
    else:
        print("Nothing found")
except requests.RequestException as e:
    print(f"Error {e}")