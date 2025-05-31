import urllib.request

t = urllib.request.urlopen("https://www.google.com").getcode()
if t == 200:
    print("website is online")
else :
    print("website is down")    

# import requests
# url = "https://w.google.com"
# r = requests.get(url)
# if r.status_code == 200 :
#     print("website is online")
# else:
#     print("website is down")     