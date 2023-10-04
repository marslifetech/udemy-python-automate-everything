# Libraries 


## PipEnv 
pip3 install python-dotenv
https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1


# Section 1 


# Section 2 
## simple scraper
targeting https://automated.pythonanywhere.com/ using selenium 

```
pip3 install selenium chromedriver
```

.find_element_by_xpath is [depresiated >>https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath] need to use driver.find_element

```
driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
```

## Dynamic Scrapper

## Login 

targeting https://automated.pythonanywhere.com/login/ 
username: automated 
password: automatedautomated


## Beautiful Soup
Extract Data from Website 
Selenium - broswer automation 


# Section 3 - Accessing / Building APIs
REST API 

* use request library to parse json 
 /.json()/ 