import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 465

sender_email = "alan25dev@gmail.com"
password = getpass.getpass("Type your password and press enter: ")
receiver_email = "youlun5525@gmail.com"

message = MIMEMultipart("alternative")
message['Subject'] = "multipart test"
message['From'] = sender_email
message['To'] = receiver_email

# Create a plain-text and HTML version of your message
text = """\
Hi, 
How are you?
This message is sent from Python.(text)
"""

html = """\
<html>
    <body>
        <p>Hi,<br>
            How are you?<br>
            <a href="http://www.realpython.com">Real Python</a>
            has many great tutorials.
        </p>
    </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )