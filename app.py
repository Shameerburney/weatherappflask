from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '3d50b594ddf9b871cc8ea27507935690'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather(city):
    # ✅ Custom city override
    if city.lower() == "randiabazz":
        return {
            'city': "Randiabazz",
            'temperature': 30,
            'description': "Sunny",
            'humidity': 40,
            'wind_speed': 3.5
        }

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)
    return render_template('index.html', weather=weather)


@app.route('/api/weather/<city>')
def api_weather(city):
    weather = get_weather(city)
    if weather:
        return jsonify(weather)
    else:
        return jsonify({'error': 'City not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
