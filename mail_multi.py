import csv, smtplib, ssl, getpass

message = """\
Subject: Your grade

Hi {name}, your grade is {grade}.
"""

from_address = "alan25dev@gmail.com"
password = getpass.getpass("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name, grade=grade),
            )



# with open("contacts_file.csv") as file:
#     reader = csv.reader(file)
#     next(reader) # Skip header row
#     for name, email, grade in reader:
#         print(f"Sending email to {name.strip()}") # 用.strip()去除頭尾空格
#         # Send email here 