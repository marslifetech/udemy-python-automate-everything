#!/bin/env python3 
## Add an embeded image in the email. 
## Referencing https://stackoverflow.com/questions/920910/sending-multipart-html-emails-which-contain-embedded-images


import smtplib
from dotenv import load_dotenv
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

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
It appear that you have been very good this year. <br>
As such, you are receiving your christmas gifts early this year.<br> 
Enjoy! <br>
<img style="width:50%;text-align:center;"  src="cid:image1"><br>
ho oh ho!
""" 
mimetext = MIMEText(body,'html')
message.attach(mimetext)

fp = open("merry-christmas.webp", "rb")
msgImg = MIMEImage(fp.read())
fp.close()
msgImg.add_header('Content-ID', '<image1>')
message.attach(msgImg)

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,message.as_string())
server.quit()

print("email sent")



