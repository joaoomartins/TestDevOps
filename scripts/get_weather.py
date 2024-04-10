import requests
import json

def get_weather(location):
        api_key = 'da4b3d88c615d7e8a3c980893c2f11bb'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

        response = requests.get(url)
        weather_data = response.json()

        return weather_data

if __name__ == "__main__":
    location = 'Portalegre'
    weather_data = get_weather(location)
    print(json.dumps(weather_data))