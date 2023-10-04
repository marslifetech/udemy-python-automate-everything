#!/bin/env python3 

import yagmail
import os 
from dotenv import load_dotenv
import pandas 

load_dotenv()
# initalize gmail variables 
sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv('GMAIL_PASSWORD')
subject = "Billing Info"

# intialize gmail ciient
yag = yagmail.SMTP(user=sender,password=password)



df = pandas.read_csv('billing.csv')

for index, row in df.iterrows(): 
    contents = [f"""
    Hello {row['name']},
    Our records show that you owe us {row['amount']}. 
    Bill is attached
    """, row['bill']]

    yag.send(to=row['email'],subject=subject,contents=contents)
    print("Email Sent")