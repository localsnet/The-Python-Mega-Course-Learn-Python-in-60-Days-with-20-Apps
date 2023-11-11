import smtplib
import ssl
import os
LOGIN="localsnet"
PASSWORD="tlwtvbxfkxjltkyb"

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    # username = os.getenv("LOGIN")
    # password = os.getenv("PASSWORD")
    username = LOGIN
    password = PASSWORD

    # receiver = f"{os.getenv('LOGIN')}@gmail.com"
    receiver = f"{username}@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)