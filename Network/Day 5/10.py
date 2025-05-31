import requests
import concurrent.futures
from bs4 import BeautifulSoup
from urllib.parse import urljoin

target = input("Enter the url: ")
wordlist = input("Enter the wordlist path: ")

def test(path):
    try:
        endpoint = urljoin(target, path)
        agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124'}
        title = None
        response = requests.get(endpoint, headers=agent, allow_redirects=False)
        soup = BeautifulSoup(response.content, "html.parser")
        tag = soup.find("title")
        title = tag.get_text(strip=True) if tag else None
        print(f"endpoint: {endpoint} ==> {response.status_code} <> {title}")
                    
    except requests.RequestException:
        pass      
def thread():
    try:
        with open(wordlist, "r")as f:
            s = [line.strip() for line in f]  
            if not s:
                print("Wordlist is empty")
                return 
            print("Finding endpoints")
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            executor.map(test, s)
    except FileNotFoundError:
        print("Wordlist does not exist.")                   
thread()