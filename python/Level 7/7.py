
sender = input("Enter the sender name: ")
domain = input("Enter the company domain: ")
recipient = input("Enter the recipient name: ")
link = "http://testphp.vulnweb.com/login.php"

def test():
    email = f"noreplay@{domain}"
    subject = "Attention, suspicious activity found! Update your account"
    body = f"""
Dear {recipient},

We have detected an issue with your account that requires your attention. To avoid suspension, please update your account details immediately by clicking the link below:

{link}

If you do not take action within 24 hours, your account may be locked. We apologize for the inconvenience and thank you for your prompt attention.

Best regards,  
{sender}  


---

"""
    return body
print(test())       