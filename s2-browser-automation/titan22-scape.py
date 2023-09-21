#!/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


def get_driver(url):
    # Set options to make browsing easier 
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("new-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.get(url)

    return driver

def clean_text(text):
    # Extract temp from text
    return float(text.split(":")[1].strip())

def main():
    driver = get_driver("https://titan22.com/account/login")
    driver.find_element("id", "CustomerEmail").send_keys("")
    time.sleep(2)
    driver.find_element("id", "CustomerPassword").send_keys("" + Keys.RETURN)

    print(driver.current_url)

print(main())