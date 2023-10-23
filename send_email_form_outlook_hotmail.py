import smtplib
from email.me.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "sender_email@hotmail.com"
receiver = "receiver_email@domian.com"
password = "sender_password"

##simple text message
# message = """
# Subject: This is email subject

# This is email content
# """

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "This is email subject"

body = """<h2> Hi there!</h2>
This is content of the body.
"""

mimetext = MIMEText(body, "html")
message.attach(mimetext)

attachement_path = 'attach_file.extension'
attachement_file = open(attachement_path, 'rb')

payload = MIMEBase('application', 'octet-stream')
payload.set_payload(attachement_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachement', filename=attachement_path)
message.attach(payload)

server = smtp.server(host="smtp.office365.com", port=587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())
server.quit()
