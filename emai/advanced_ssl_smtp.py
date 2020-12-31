import smtplib
import ssl
from email.message import EmailMessage


def collect():
    return input("Enter your email : "), \
           input("Enter your password : "), \
           input("Enter receiver's address : "), \
           input("Enter the Subject : "), \
           input("Enter your message : ")


MAIL_ADDR, MAIL_PWD, receiver, subject, body, = collect()
msg = EmailMessage()
msg['Subject'] = subject
msg['from'] = MAIL_ADDR
msg['to'] = receiver
msg.set_content(body)
msg.add_alternative(f"""
    <!DOCTYPE html>
    <html>
        <body>
            <h1>{body}</h1>
        </body>
    </html>
""", subtype='html')

if MAIL_ADDR and MAIL_PWD:
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(MAIL_ADDR, MAIL_PWD)
        server.send_message(msg)
