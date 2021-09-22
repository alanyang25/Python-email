import email, smtplib, ssl, getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 465

subject = "An email with attchment from Python"
body = "This is an email with attachment from Python."
sender_email = "alan25dev@gmail.com"
password = getpass.getpass("Type your password and press enter: ")
receiver_email = "youlun5525@gmail.com"

# Create a multipart message and set headers
message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email
message['Bcc'] = receiver_email # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "Python Testing with Pytest.pdf" # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment 
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)