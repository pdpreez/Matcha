import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def verMail(receiver_email, passcode):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "Matcha verification."
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

def likeMail(receiver_email):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "Someone likes you."
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
    <html>
    <p>Someone liked your profile. Click
    <a href='http://localhost:5000/login'>login</a>
    to see who it was, it could be a match!</p>
    </html>
    """
    part = MIMEText(text, "html")
    message.attach(part)
    email_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=email_context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def matchMail(receiver_email, user):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "You just matched with..."
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
    <html>
    <p>You just matched with {}!!! Click
    <a href='http://localhost:5000/login'>login</a>
    to start talking to them.</p>
    </html>
    """.format(user)
    part = MIMEText(text, "html")
    message.attach(part)
    email_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=email_context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def unmatchMail(receiver_email):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "Unlucky mate"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
    <html>
    <p>Someone just unmatched you, and also your popularity decreased. Click
    <a href='http://localhost:5000/login'>login</a>
    to see who.</p>
    </html>
    """
    part = MIMEText(text, "html")
    message.attach(part)
    email_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=email_context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def viewMail(receiver_email):
    port = 465
    sender_email = "noreply.matcha2019@gmail.com"
    # For testing, use jeansthebeans@mailinator.com
    password = ""
    message = MIMEMultipart("aleternative")
    message["Subject"] = "Someone just viewed your profile."
    message["From"] = sender_email
    message["To"] = receiver_email
    text = """
    <html>
    <p>You too can view profiles. Simply 
    <a href='http://localhost:5000/login'>login</a>
    now.</p>
    </html>
    """
    part = MIMEText(text, "html")
    message.attach(part)
    email_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=email_context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())