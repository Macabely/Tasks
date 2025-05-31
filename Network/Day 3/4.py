import requests
import time
def test(url):
    s = time.perf_counter()
    r = requests.get(url)
    e = time.perf_counter()
    total = (e - s) * 1000
    totals = r.elapsed.total_seconds() * 1000
    print(f"Total time to {url}: {total} ms")
    print(f"Total time to {url}: {totals} ms")
    
test("https://www.google.com")