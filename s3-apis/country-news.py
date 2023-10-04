#!/bin/env python3
import os
import requests 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NEWS_API_KEY')

def get_news(country, api_key=api_key):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    
    results = []
    for article in articles:
        results.append(f"TITLE:\n{article['title']}\n DESCRIPTION:\n{article['description']}\n\n")
    
    return results

    
print(get_news(country="us"))