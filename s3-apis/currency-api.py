#!/bin/env python3 

from flask import Flask, jsonify
import requests 
from bs4 import BeautifulSoup 



def get_currency_convertion(currencyFrom,currencyTo):
    url = f"https://www.x-rates.com/calculator/?from={currencyFrom}&to={currencyTo}&amount=1"
    content = requests.get(url).content

    soup = BeautifulSoup(content, 'html.parser')
    rate = float(soup.find("span", class_="ccOutputRslt").get_text().split(" ")[0])

    return rate


app = Flask(__name__)



@app.route('/')
def home():
    return '<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate = get_currency_convertion(in_cur,out_cur)
    return jsonify({"input_currency": in_cur,"output_currency":out_cur,"rate":rate})

app.run()