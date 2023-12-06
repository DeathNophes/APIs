import datetime as dt
import requests
key = ''

"""
You need to create a registration at https://openweathermap.org/ to get a unique APIkey
"""


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


city = input()

url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}'
response = requests.get(url).json()

country = response['sys']['country']
temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius(temp_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"The weather in {city}, {country}:\n"
      f"- Temperature in {city} is {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F\n"
      f"- General weather in {city} is {description}\n"
      f"- Humidity in {city} is {humidity}%\n"
      f"- The sunrise is at {sunrise_time} local time\n"
      f"- The sunset is at {sunset_time} local time")

"""
Example output:
The weather in Sofia, BG:
- Temperature in Sofia is 5.31°C or 41.56°F
- General weather in Sofia is overcast clouds
- Humidity in Sofia is 88%
- The sunrise is at 2023-12-06 07:42:04 local time
- The sunset is at 2023-12-06 16:53:21 local time
"""
