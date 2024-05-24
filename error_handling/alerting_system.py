import smtplib
from email.mime.text import MIMEText

def send_alert(email_recipient, subject, message):
    sender = "your-email@example.com"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = email_recipient

    with smtplib.SMTP("localhost") as server:
        server.sendmail(sender, [email_recipient], msg.as_string())

# Example usage
send_alert("recipient@example.com", "Test Alert", "This is a test alert message.")

