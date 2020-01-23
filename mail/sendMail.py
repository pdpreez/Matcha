import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def verMail(receiver_email, passcode):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "Test email."
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
    <html>
    <p>Click the link below to verify your account.</p>
    <a href='http://localhost:5000/verify?email={}&uuid={}'>Matcha</a>
    </html>
    """.format(receiver_email, passcode)
    part = MIMEText(text, "html")
    message.attach(part)
    email_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=email_context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
