#!/bin/env python3 

import yagmail 
from dotenv import load_dotenv
import os
import time
from datetime import datetime as dt

load_dotenv()



sender = "mjuchytil@gmail.com"
password = os.getenv("GMAIL_PASSWORD")
receiver = "mjuchytil@outlook.com"

subject = "This a test email"

contents = """
Here is the contents of this email. 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=password )

while True: 
    now = dt.now()
    print(f" {now.hour}  {now.minute}")
    if now.hour == 22 and now.minute == 47: 
        yag.send(to=receiver,subject=subject, contents=contents)
        print("email sent")
    time.sleep(60)