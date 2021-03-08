from matplotlib.figure import Figure

from Weather import Weather
from tkinter import *
from PIL import ImageTk as itk
from PIL import Image
import datetime

import numpy as np
import matplotlib.pyplot as plt
from calendar import monthrange
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import pandas as pd



class WeatherDisplayUI:
    def __init__(self, weather=Weather()):
        self.weather = weather

        pass

    def create_ui(self):
        tk = Tk()
        tk.size = (600, 800)
        tk.resizable(width=False, height=False)
        tk.geometry = (600, 800)
        basewidth = 700
        img = Image.open('sky.jpg')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save('skyResized.jpg')

        background = "skyResized.jpg"
        img = itk.PhotoImage(file=background)
        canvas = Canvas(tk, width=600,
                        height=400)

        canvas.pack(fill="both", expand=True)

        canvas.create_image(0, 0, image=img,
                            anchor="nw")

        title_string = self.weather.location
        title_label = canvas.create_text(tk.size[0] / 2, 30, text=title_string, font=("Purisa", 32), fill='white',
                                         anchor='center')

        temperature_string = "Temperature: " + '{:.2f}'.format(((self.weather.get_temperature_fahrenheit())))
        temperature_label = canvas.create_text(10, 60, text=temperature_string, font=("Purisa", 16), fill='white',
                                               anchor='nw')

        feels_string = "Feels like: " + '{:.2f}'.format((self.weather.get_feels_fahrenheit()))
        temperature_label = canvas.create_text(10, 90, text=feels_string, font=("Purisa", 16), fill='white',
                                               anchor='nw')

        weather_string = "Condition: " + self.weather.get_forecast()
        weather_label = canvas.create_text(10, 120, text=weather_string, font=("Purisa", 16), fill='white',
                                           anchor='nw')
        now = datetime.datetime.now()

        canvas.create_text(500, 10, text="Hourly Forecast: ", fill='white', anchor='w')
        count = 0
        for s in self.weather.hourly_forecast:
            placeholder = str((now.hour + count) % 25) + ": " + s
            canvas.create_text(500, 30+(count * 10), text=placeholder, fill='white', anchor='w')
            count += 1
            if count > 24:
                break

        canvas_2 = Canvas(tk, width=400,
                          height=400, bg='blue')
        canvas_2.pack(fill="both", expand=True)

        counter = 0
        axis = []
        values = []
        for s in self.weather.hourly_temps:
            t = counter + now.hour
            axis.append(str(t))
            values.append(s)
            counter += 1
            if counter >= 24:
                break

        data = {'Hour': axis, 'Temperature(f)': values}
        df = pd.DataFrame(data, columns=['Hour', 'Temperature(f)'])
        fig = Figure(figsize=(2, 2), dpi=100)

        ax = fig.add_subplot(111)
        ax.set_title('Hourly Temperature')
        major_ticks = np.arange(0, 101, 1)
        minor_ticks = np.arange(0, 101, 1)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        ax.grid(which='both')

        ax.grid(which='minor', alpha=0.4)
        ax.grid(which='major', alpha=0.6)

        plt.show()

        chart_type = FigureCanvasTkAgg(fig, canvas_2)

        chart_type.get_tk_widget().pack(side=BOTTOM, fill=BOTH)

        df = df[['Hour', 'Temperature(f)']].groupby('Hour').sum()

        df.plot(kind='line', legend=True, ax=ax)

        fig.canvas.draw()

        tk.mainloop()
        pass


def get_lowest(arr):
    lowest = 250
    for a in arr:
        if a < lowest:
            lowest = a
    return lowest


def get_highest(arr):
    highest = -100
    for a in arr:
        if a > highest:
            highest = a
    return highest