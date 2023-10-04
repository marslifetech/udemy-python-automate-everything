#!/bin/env python3
import os
import requests 
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv('NEWS_API_KEY')

r = requests.get(f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={apiKey}")
content = r.json()
print(content['articles'][0]['title'])