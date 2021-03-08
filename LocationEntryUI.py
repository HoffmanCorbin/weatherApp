from tkinter import *

from Api import Api
from PIL import ImageTk as itk
from PIL import Image

from Weather import Weather
from WeatherDisplayUI import WeatherDisplayUI


class LocationEntryUI:

    def __init__(self):
        self.tk = Tk()

        basewidth = 700
        img = Image.open('image.jpg')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save('imageResized.jpg')

        self.tk.geometry("400x400")
        background = "imageResized.jpg"
        img = itk.PhotoImage(file=background)
        canvas1 = Canvas(self.tk, width=400,
                         height=400)

        canvas1.pack(fill="both", expand=True)

        canvas1.create_image(0, 0, image=img,
                             anchor="nw")

        self.tk.title('Weather')

        city_lbl = canvas1.create_text(20, 20, font=("Purisa", 16), fill='white', text="City", anchor='nw')
        city_field = Text(self.tk, height=2, width=20, bg='lightgrey')
        city_field.pack()
        button3_canvas = canvas1.create_window(20, 50, anchor="nw",
                                               window=city_field)

        state_lbl = canvas1.create_text(20, 100, font=("Purisa", 16), fill='white', text="State", anchor='nw')
        state_field = Text(self.tk, height=2, width=20, bg='lightgrey')
        state_field.pack()
        state_field_canvas = canvas1.create_window(20, 130, anchor="nw", window=state_field)

        button = Button(self.tk, text='Continue', width=25, bg = 'lavender',
                        command=lambda: self.get_weather_info(city_field.get("1.0", 'end-1c'),
                                                              state_field.get("1.0", 'end-1c')))

        button1_canvas = canvas1.create_window(20, 200,
                                               anchor="nw",
                                               window=button)

        title_lbl = canvas1.create_text(300, 100, text="Just Another\nWeather App",
                                        font=("Purisa", 24), fill = 'grey91')

        self.tk.mainloop()

        pass

    def get_weather_info(self, city, state):
        api = Api()
        w = Weather()
        w = api.get_currentWeather(city + ", " + state)

        self.tk.destroy()
        weather_ui = WeatherDisplayUI(w)
        weather_ui.create_ui()


        pass
