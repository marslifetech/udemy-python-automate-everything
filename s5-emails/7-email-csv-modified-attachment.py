#!/bin/env python3

import os 
import pandas 
from dotenv import load_dotenv
import yagmail

# query .env file 
load_dotenv()

# intalize gmail info 
sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv('GMAIL_PASSWORD')
subject = "Billing Info"

# Initialize gmail client 
yag = yagmail.SMTP(user=sender, password=password)

# read csv file 
df = pandas.read_csv('modified.csv')
 

def generate_file(content,filename):
    with open(filename, "w") as file:
        file.write(content)
        file.close()


for index,row in df.iterrows():
    name = row['name']
    amount = row['amount']
    filepath = f"bills/{row['name']}.txt"
    email = row['email']

    contents = [f"""Hello {name},
    Our records indicate that you owe us ${amount}. 
    Attached is your bill""", filepath]

    generate_file(content=str(amount),filename=filepath)
    yag.send(to=email, subject=subject,contents=contents)