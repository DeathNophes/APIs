import datetime as dt
import requests
from tkinter import *

key = ''

"""
You need to create a registration at https://openweathermap.org/ to get a unique APIkey
"""


class Weather:
    def __init__(self, city):
        self.city = city

    def weather_info(self):
        url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={self.city}'

        try:
            response = requests.get(url)
            data = response.json()

            temp_kelvin = float(data['main']['temp'])
            temp_celsius = temp_kelvin - 273.15
            temp_fahrenheit = temp_celsius * (9/5) + 32

            print(f"The weather in {self.city}, {data['sys']['country']}\n"
                  f"- General weather: {data['weather'][0]['description']}\n"
                  f"- Temperature is: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F\n"
                  f"- Sunrise is at: {dt.datetime.utcfromtimestamp(data['sys']['sunrise'])} local time\n"
                  f"- Sunset is at: {dt.datetime.utcfromtimestamp(data['sys']['sunset'])} local time\n")

        except requests.exceptions.RequestException as e:
            print('Error'), e


"""
Our Window
"""

main_window = Tk()
main_window.title("Checking the weather")
main_window.geometry("300x300")

"""
Labels on the first row
"""

bulgaria = Label(main_window, text="Bulgaria")
bulgaria.grid(row=0, column=0, columnspan=3, padx=50, pady=20)
europe = Label(main_window, text="Europe")
europe.grid(row=0, column=3, columnspan=3, padx=50, pady=20)

"""
Here are the Buttons
"""

# For Bulgaria
sofia = Weather('Sofia')
sofia_button = Button(main_window, text="Sofia", padx=10, pady=5, command=sofia.weather_info)
sofia_button.grid(row=1, column=1)
plovdiv = Weather('Plovdiv')
plovdiv_button = Button(main_window, text="Plovdiv", padx=4, pady=5, command=plovdiv.weather_info)
plovdiv_button.grid(row=2, column=1)
varna = Weather('Varna')
varna_button = Button(main_window, text="Varna", padx=8, pady=5, command=varna.weather_info)
varna_button.grid(row=3, column=1)
burgas = Weather('Burgas')
burgas_button = Button(main_window, text="Burgas", padx=5, pady=5, command=burgas.weather_info)
burgas_button.grid(row=4, column=1)
pernik = Weather('Pernik')
pernik_button = Button(main_window, text="Pernik", padx=7, pady=5, command=pernik.weather_info)
pernik_button.grid(row=5, column=1)

# For Europe
berlin = Weather('Berlin')
berlin_button = Button(main_window, text="Berlin", padx=7, pady=5, command=berlin.weather_info)
berlin_button.grid(row=1, column=4)
zurich = Weather('Zurich')
zurich_button = Button(main_window, text="Zurich", padx=5, pady=5, command=zurich.weather_info)
zurich_button.grid(row=2, column=4)
paris = Weather('Paris')
paris_button = Button(main_window, text="Paris", padx=10, pady=5, command=paris.weather_info)
paris_button.grid(row=3, column=4)
rome = Weather('Rome')
rome_button = Button(main_window, text='Rome', padx=7, pady=5, command=rome.weather_info)
rome_button.grid(row=4, column=4)
brussels = Weather('Brussels')
brussels_button = Button(main_window, text='Brussels', padx=3, pady=5, command=brussels.weather_info)
brussels_button.grid(row=5, column=4)

main_window.mainloop()