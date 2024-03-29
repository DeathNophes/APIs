import requests
from tkinter import *

key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


def get_stock_price():
    stock_name = asset_entry.get()
    display.delete(0, 'end')
    url = f"https://api.twelvedata.com/time_series?symbol={stock_name}&interval=1min&apikey={key}"

    try:
        request = requests.get(url)
        data = request.json()

        if data['status'] == 'error':
            display.insert(0, 'Error! Enter a valid stock!')
        else:
            display.insert(0, f"{data['meta']['symbol']} "
                              f"- Current price (USD): {data['values'][0]['close']}")

    except requests.exceptions.RequestException as e:
        display.insert(0, 'Error'), e


"""
Our Window
"""

main_window = Tk()
main_window.title("Crypto price API")
main_window.geometry("500x300")
main_window.config(bg="#85929E")


"""
Our Entries and Buttons
"""

asset_entry = Entry(main_window, width=40)
get_button = Button(main_window, text='Get', bg='yellow', width=20, command=get_stock_price)
display = Entry(main_window, width=50)

asset_entry.pack(pady=10)
get_button.pack(pady=5)
display.pack(pady=50)

main_window.mainloop()

"""
Example output:
AAPL - Current price (USD): 184.36000
"""