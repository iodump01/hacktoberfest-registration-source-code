import smtplib
import ssl

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(receiverEmail, subjectEmail, html_content):
    subject = subjectEmail
    # Sender's Email Address
    sender_email = "email@gmail.com"
    receiver_email = receiverEmail
    # Sender's Password
    password = "password"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html_content, "html", 'utf-8'))

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.send_message(message)
        return "Mail send"
