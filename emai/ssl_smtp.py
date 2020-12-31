import smtplib
import ssl


def collect():
    return input("Enter your username : "), \
           input("Enter your password : "), \
           input("Enter your message : "), \
           input("Enter receiver's address : ")


username, password, message, receiver = collect()
port = 465

if len(username) > 1 and len(password) > 1:
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
