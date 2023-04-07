from dotenv import load_dotenv
import os
load_dotenv()
import smtplib

SENDER_EMAIL = os.getenv('EMAIL')
SENDER_PASSWORD = os.getenv('PASSWORD')

SMTP = 'smtp.gmail.com'
PORT = 587

def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP(SMTP, PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

#===========================================
receiver_email = []
subject = 'Python Masterclass - TEST'
body = 'This is an email sent with Python.'

send_email(receiver_email, subject, body)
