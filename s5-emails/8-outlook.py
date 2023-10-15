#!/bin/env python3 

import smtplib
import os 
from dotenv import load_dotenv

load_dotenv()

# initalize smtp client variables 
sender = os.getenv('OUTLOOK_ACCOUNT')
password = os.getenv('OUTLOOK_PASSWORD')
receiver = os.getenv('GMAIL_ACCOUNT')


message = """\
Subject: Hello World

Hello, this is a test of the weather broadcasting service. 
Testing.
"""


server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,message)
server.quit()
print('sent email  ')