#!/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime 
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
    """"Extract only the Temperature from Text"""
    # Extract temp from text
    return float(text.split(":")[1].strip())

def write_file(fileName,text):
    """"Write Input to text into a text file"""
    file = open(f"{fileName}.txt", "w")
    file.write(str(text))
    file.close()


def main():
    driver = get_driver("https://automated.pythonanywhere.com/login/")
    driver.find_element("id", "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element("id", "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element("xpath", "/html/body/nav/div/a").click()
    time.sleep(2)
    
    while True:
        element = driver.find_element("xpath", "/html/body/div[1]/div/h1[@id='displaytimer']")
        fileName = datetime.now().strftime("%Y-%m-%d.%H-%M-%S")
        write_file(fileName,clean_text(element.text))
        time.sleep(2)

main()
