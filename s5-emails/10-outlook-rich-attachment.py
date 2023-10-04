#!/bin/env python3 

import smtplib
from dotenv import load_dotenv
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


load_dotenv()

sender = os.getenv('OUTLOOK_ACCOUNT')
password = os.getenv('OUTLOOK_PASSWORD')
receiver = os.getenv('GMAIL_ACCOUNT')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Merry Christmas!"

body = """
<h1>Hello There!</h1> 
It appear that you have been very good this year. 
As such, you are receiving your christmas gifts early this year. 
Enjoy! 

ho oh ho!
""" 
mimetext = MIMEText(body,'html')
message.attach(mimetext)

attachment_path = "merry-christmas.webp"
attachment_file = open(attachment_path,'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
payload.add_header('Content-Disposition','attachment', filename=attachment_path)
encoders.encode_base64(payload)
message.attach(payload)
message_text = message.as_string()


server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,message_text)
server.quit()

print("email sent")



