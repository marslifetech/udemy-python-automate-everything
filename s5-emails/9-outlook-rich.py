#!/bin/env python3 

import os 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


load_dotenv()

sender = os.getenv('OUTLOOK_ACCOUNT')
password = os.getenv('OUTLOOK_PASSWORD')
receiver = os.getenv('GMAIL_ACCOUNT')


message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello Again"

body = """
<h1>Hello There</h1>
There seems to be an overabunance of cat photos in the world. 
That being said, one more couldn't hurt...
"""

mimetext = MIMEText(body, 'html')

message.attach(mimetext)

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
message_text = message.as_string()
server.sendmail(sender,receiver,message_text)
server.quit()

print('email sent')