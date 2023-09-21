#!/bin/env python3

import requests 
from bs4 import BeautifulSoup 

currencyFrom = input("Please input the currency you would like to convert from: ")
currencyTo = input("Please input the currency you would like to convert to: ")


def getCurrencyConvertion(currencyFrom,currencyTo):
    url = f"https://www.x-rates.com/calculator/?from={currencyFrom}&to={currencyTo}&amount=1"
    content = requests.get(url).content

    soup = BeautifulSoup(content, 'html.parser')
    rate = float(soup.find("span", class_="ccOutputRslt").get_text().split(" ")[0])

    return rate

print(getCurrencyConvertion(currencyFrom,currencyTo))