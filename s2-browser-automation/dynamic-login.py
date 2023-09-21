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
    driver = get_driver("https://automated.pythonanywhere.com/login/")
    driver.find_element("id", "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element("xpath", "/html/body/nav/div/a").click()
    time.sleep(2)
    element = driver.find_element("xpath", "/html/body/div[1]/div/h1[@id='displaytimer']")

    return clean_text(element.text)

print(main())