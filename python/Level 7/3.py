import requests
from bs4 import BeautifulSoup

url = "http://testphp.vulnweb.com/login.php"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")
links = set()

for link in soup.find_all(["a", "link"], href=True):
    links.add(link["href"])

for link in soup.find_all(src=True):
    links.add(link["src"])    

print("Extracted links:")
for link in sorted(links):
    print(link)