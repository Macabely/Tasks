import requests
def test():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    url = "http://testphp.vulnweb.com/userinfo.php"
    data = {"uname": username, "pass": password}
    response = requests.post(url, data=data)
    if '<input name="uname"' not in response.text:
        print(f"Successful login, welcome: {username}")
    else:
        print("Weong credintials")        
test()    