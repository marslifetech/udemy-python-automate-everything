#!/bin/env python3

import yagmail 
import os 
from dotenv import load_dotenv
import pandas
from datetime import datetime
import time
load_dotenv()

#configure variables 
sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv('GMAIL_PASSWORD')
df = pandas.read_csv('emails.csv')

yag = yagmail.SMTP(user=sender, password=password)
subject = "Merry Christmas!"


while True: 
    now = datetime.now()
    print(now.hour)
    if now.hour == 5: 
        for index,row in df.iterrows(): 
            content = [f"""
            Hello {row['name']}. Hope you are doing well. 
            I bet you would do even better with a few gifts to cheer you up!
            Merry Christmas!""","merry-christmas.webp"]
            yag.send(to=row['email'],contents=content,subject=subject)
            print(f"sent email to {row['name']}")
    time.sleep(3600) 