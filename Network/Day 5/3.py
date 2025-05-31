import urllib.request

try:
    t = urllib.request.urlopen("https://www.google.com").getcode()
    if 500 <= t <= 599:
        print("website is down")
    else:
        print("website is up")
except urllib.error.URLError:
    print("website is down")