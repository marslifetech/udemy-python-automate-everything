#!/bin/env python3 

import yagmail 
from dotenv import load_dotenv
import os
import pandas


load_dotenv()

sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv("GMAIL_PASSWORD")

subject = "Testing Email"




df = pandas.read_csv('emails.csv')

yag = yagmail.SMTP(user=sender,password=password)

for index, row in df.iterrows(): 
    contents = f"""
    Hello {row['name']}!  Testing this email string. 
    """
    yag.send(to=row['email'],subject=subject,contents=contents)
    print("email sent")
