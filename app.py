from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)
app.debug = True

@app.route('/weather_dashboard')
def weather_dashboard():
    return render_template('index.html')

@app.route('/weather_results', methods=['POST'])
def weather_results():
    city_name = request.form['cityName']
    api_key = get_api_key()
    data = get_weather_results(city_name, api_key)
    temp_fahreinheit = "{0:.2f}".format(data["main"]["temp"])
    print(temp_fahreinheit)
    feels_like_f = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    temp_celsius = covert_to_celsius(float(temp_fahreinheit))
    print(temp_celsius)
    feels_like_c = covert_to_celsius(float(feels_like_f))

    return render_template('results.html',
                           location=location, temp_celsius=temp_celsius,
                           feels_like_c=feels_like_c, weather=weather)

def covert_to_celsius(temp_faren):
    result = ((temp_faren - 32) * 5.0/9.0)/10
    return round(result, 2)

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
