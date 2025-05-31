import requests
from bs4 import BeautifulSoup

url = "http://testphp.vulnweb.com/login.php"
req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

for link in soup.find_all(["title"]):
    print(link.text)