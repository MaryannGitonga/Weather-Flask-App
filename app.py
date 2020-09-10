import requests
import configparser

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city_name, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()
    
print(get_weather_results("Nairobi", get_api_key())
