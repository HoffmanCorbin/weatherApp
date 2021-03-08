import requests
import json

from Weather import Weather


class Api:

    def __init__(self):
        self.apiKey = ""
        self.lat = 0
        self.long = 0
        pass

    def get_apikey(self):
        return self.apiKey

    def get_currentWeather(self, city):
        env = open("dat.env", "r")
        self.apiKey = env.read()

        resp = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + self.apiKey)
        temp = resp.json()['main']
        temperature = temp['temp']
        feels = temp['feels_like']
        weather_json = resp.json()['weather']
        weather = weather_json[0]['main']
        disc = weather_json[0]['description']
        location = resp.json()['name']
        weather = Weather(temperature, feels, weather, disc, location)

        coord = resp.json()['coord']
        self.lat = coord['lat']
        self.long = coord['lon']
        weather = self.get_temperature_daily(weather)
        return weather

    # Requires get_currentWeather to be called first
    def get_temperature_daily(self, weather):
        resp = requests.get(
            'https://api.openweathermap.org/data/2.5/onecall?lat=' + str(self.lat) + '&lon=' + str(
                self.long) + "&appid=" + self.apiKey)

        hourly = resp.json()['hourly']
        temps = []
        weathers = []
        for b in hourly:
            temps.append((b['temp'] - 273.15) * (9 / 5) + 32)
            c = (b['weather'])
            c = c[0]
            c = c['main']
            weathers.append(c)

        weather.set_hourly_temperature(temps)
        weather.hourly_forecast = weathers
        return weather



