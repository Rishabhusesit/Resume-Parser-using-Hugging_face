import smtplib
from email.message import EmailMessage

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "rishabh.09919011722@ipu.ac.in"
    msg["To"] = recipient

    with smtplib.SMTP("rishabh.09919011722@ipu.ac.in.gmail.com", 587) as server:
        server.starttls()
        server.login("rishabh.09919011722@ipu.ac.in", "Rishabh@05")
        server.send_message(msg)
