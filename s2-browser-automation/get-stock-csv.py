#!/bin/env python3 

import requests 
from datetime import datetime
import time 

ticker = input("Enter Stock Ticker Symbol: ")
fromDate = input("Enter start date in yyyy/mm/dd format: ")
toDate = input("Enter end date in yyyy/mm/dd format: ")

fromDateTime = datetime.strptime(fromDate, '%Y/%m/%d')
toDateTime = datetime.strptime(toDate, '%Y/%m/%d')

fromEpoch = int(time.mktime(fromDateTime.timetuple()))
toEpoch = int(time.mktime(toDateTime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={fromEpoch}&period2={toEpoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content

with open(f'{ticker}.csv','wb') as file:
    file.write(content)