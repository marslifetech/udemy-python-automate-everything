#!/bin/env python3 

import os 
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')

def get_weather(city, api_key=api_key):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    r = requests.get(url)
    weather_data = r.json()

    return weather_data

def format_data(data_points):
    formated_data = ["City,Time,Temperature,Condition"]
    for data in data_points['list']:
        dt = data['dt_txt']
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        city = data_points['city']['name']
        formated_data.append(f"{city},{dt},{temp},{condition}")
    return formated_data

def write_list_to_file(list,file_name):
    file = open(file_name,"w")
    for item in list: 
        file.write(f"{item}\n")
    file.close()



weather_data = get_weather(city="milwaukee" )
formated_weather_data = format_data(weather_data)
write_list_to_file(formated_weather_data,"data.txt")

