import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email, from_email, password, smtp_server='smtp.gmail.com', port=587):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)