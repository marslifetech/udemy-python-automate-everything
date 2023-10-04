#!/bin/env python3 
 
from selenium import webdriver
import time 
import yagmail
import os 
from dotenv import load_dotenv


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("disable-infobars")
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('new-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options)
    driver.get(url)

    return driver


url = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"

load_dotenv()

sender = os.getenv('GMAIL_ACCOUNT')
password = os.getenv('GMAIL_PASSWORD')
receiver = os.getenv('OUTLOOK_ACCOUNT')


while True:
    driver = get_driver(url)
    time.sleep(1)
    element = driver.find_element("xpath", "/html/body/div[2]/div/section[1]/div/div/div[2]/span[2]")
    stock_change_percentage = float(element.text.split(" ")[0])

        
    if stock_change_percentage < -0.12: 
        yag = yagmail.SMTP(sender,password)
        subject = "Currently losing Money"
        contents = f"""It appears that your stock is currenctly losing money
        It is currently at {stock_change_percentage}%"""

        yag.send(receiver,subject=subject,contents=contents)
        print("email sent")

    time.sleep(60)



