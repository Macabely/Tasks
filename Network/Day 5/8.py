import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

site = input("Enter the root domain url: ")
save = input("Where you gonna save the images: ")

try:

    response = requests.get(site)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    tags = soup.find_all('img') 

    for img in tags:
        src = img.get('src') or img.get('data-src')
        if src:
            full = urljoin(site, src)
            filename = os.path.basename(full.split('?')[0])
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                continue
            file = os.path.join(save, filename)
            try:
                test = requests.get(full)
                if test.status_code == 200:
                    with open(file, 'wb') as f:
                        f.write(test.content)
                    print(f"Downloaded: {filename}")
            except requests.RequestException:
                print(f"Failed: {filename}")

except requests.RequestException as e:
    print(f"Failed to fetch {site}: {e}")