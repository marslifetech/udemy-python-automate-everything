#!/bin/env python3

import requests 
from dotenv import load_dotenv
import os 

load_dotenv()

api_token = os.getenv('FACEBOOK_API_TOKEN')

url = f"https://graph.facebook.com/v18.0/me?fields=id%2Cname%2Cposts&access_token={api_token}"

response = requests.get(url)

print(response.text)