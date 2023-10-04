#!/bin/env python3
 
import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv('GMAIL_PASSWORD')

yag = yagmail.SMTP(user=sender, password=password)

receiver = "mjuchytil@outlook.com"
subject = "Testing Attachments"
contents = ["""
Testing this attachment feature.
""","attachment.txt", "cat.webp"]

yag.send(to=receiver, subject=subject, contents=contents)
print("email sent")