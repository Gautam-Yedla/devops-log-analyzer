import os
import smtplib
from email.message import EmailMessage

def send_email(
    *,
    subject,
    body,
    from_email=None,
    to_email=None,
    password=None,
    smtp_server="smtp.gmail.com",
    port=587
):
    # Use provided args or fallback to environment
    from_email = from_email or os.getenv("EMAIL_FROM") or os.getenv("EMAIL_USER")
    to_email = to_email or os.getenv("EMAIL_TO") or from_email
    password = password or os.getenv("EMAIL_PASS")

    # Ensure all critical vars are present
    if not from_email or not password:
        raise ValueError("EMAIL_FROM/EMAIL_USER and EMAIL_PASS must be set in environment variables or passed explicitly.")

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise
