class Weather:
    def __init__(self, temperature=0, feels = 0, forecast="", description = "" , location = ""):
        self.temperature = temperature
        self.forecast = forecast
        self.description = description
        self.feels = feels
        self.location = location
        self.daily_temps = []
        self.hourly_temps = []
        self.daily_forecast = []
        self.hourly_forecast = []
        pass

    def get_temperature_fahrenheit(self):
        return (self.temperature-273.15) * (9/5) + 32

    def get_feels_fahrenheit(self):
        return (self.feels - 273.15) * (9 / 5) + 32

    def get_forecast(self):
        return self.forecast

    def set_hourly_temperature(self, temps):
        self.hourly_temps = temps
        pass

