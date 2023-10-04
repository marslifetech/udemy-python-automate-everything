#!/bin/env python3

import requests 


url = 'https://api.languagetool.org/v2/check'
data = {
    'text' : 'Tis is a nixe day',
    'language': 'auto'
}


reponse = requests.post(url,data=data)
print(reponse.text)