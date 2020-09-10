from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)
app.debug = True

@app.route('/weather_dashboard')
def weather_dashboard():
    return render_template('index.html')

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city_name, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run()
