#!/bin/env python3
import os
import requests 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NEWS_API_KEY')

def get_news(topic, from_date, to_date, language="en", api_key=api_key):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    
    results = []
    for article in articles:
        results.append(f"TITLE:\n{article['title']}\n DESCRIPTION:\n{article['description']}\n\n")
    
    return results

    
print(get_news(topic="bitcoin",from_date="2023-08-23",to_date="2023-09-17"))