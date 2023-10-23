import yagmail

sender = "sendera@gmail.com"
receiver = "receiver@gmail.com" 

subject = "Test email send using Python"
contents = ["""Hello World :)""","attachement_file.ext"]

ya = yagmail.SMTP(user=sender, password=os.getenv('sender_email_password'))) #need to add app in gmail app and generate special password to use here
ya.send(to=receiver, subject=subject, contents=contests)
print("Email sent successfully")