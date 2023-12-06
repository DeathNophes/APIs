import requests
from tkinter import *

key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


class Assets:
    def __init__(self, symbol):
        self.symbol = symbol

    # Forex pairs
    def forex_pair(self):
        url = f"https://api.twelvedata.com/exchange_rate?symbol={self.symbol}&apikey={key}"
        try:
            request = requests.get(url)
            data = request.json()

            print(f"{data['symbol']} -> {data['rate']}")

        except requests.exceptions.RequestException as e:
            print('Error'), e

    # Stocks
    def get_stock(self):
        url = f"https://api.twelvedata.com/time_series?symbol={self.symbol}&interval=1min&apikey={key}"
        try:
            request = requests.get(url)
            data = request.json()

            print(f"Asset: {data['meta']['symbol']}\n"
                  f"--Current value (USD): {data['values'][0]['close']}\n"
                  f"--Last refreshed: {data['values'][0]['datetime']}")

        except requests.exceptions.RequestException as e:
            print('Error'), e

    # Cryptocurrencies
    def get_crypto(self):
        url = f"https://api.twelvedata.com/exchange_rate?symbol={self.symbol}&apikey={key}"
        try:
            request = requests.get(url)
            data = request.json()

            print(f"{data['symbol']} -> {data['rate']}")

        except requests.exceptions.RequestException as e:
            print('Error'), e


"""
Our Window
"""

main_window = Tk()
main_window.title("Assets management")
main_window.geometry("500x300")

"""
Labels on the first row
"""

forex_pairs = Label(main_window, text='Forex pairs:')
forex_pairs.grid(row=0, column=0, columnspan=3, padx=50, pady=20)
assets = Label(main_window, text='Assets:')
assets.grid(row=0, column=3, columnspan=3, padx=50, pady=20)
cryptocurrency = Label(main_window, text='Cryptocurrency')
cryptocurrency.grid(row=0, column=6, columnspan=3, padx=50, pady=50)

"""
Here are the buttons
"""

# For Forex
eur_usd = Assets('EUR/USD')
eur_usd_button = Button(main_window, text='EUR/USD', padx=5, pady=5, command=eur_usd.forex_pair)
eur_usd_button.grid(row=1, column=1)
eur_bgn = Assets('EUR/BGN')
eur_bgn_button = Button(main_window, text='EUR/BGN', padx=4, pady=5, command=eur_bgn.forex_pair)
eur_bgn_button.grid(row=2, column=1)
usd_jpy = Assets('USD/JPY')
usd_jpy_button = Button(main_window, text='USD/JPY', padx=6, pady=5, command=usd_jpy.forex_pair)
usd_jpy_button.grid(row=3, column=1)
usd_rub = Assets('USD/RUB')
usd_rub_button = Button(main_window, text='USD/RUB', padx=5, pady=5, command=usd_rub.forex_pair)
usd_rub_button.grid(row=4, column=1)


# For Stocks
apple = Assets('AAPL')
apple_button = Button(main_window, text='APPLE', padx=6, pady=5, command=apple.get_stock)
apple_button.grid(row=1, column=4)
google = Assets('GOOGL')
google_button = Button(main_window, text='GOOGL', padx=3, pady=5, command=google.get_stock)
google_button.grid(row=2, column=4)
microsoft = Assets('MSFT')
microsoft_button = Button(main_window, text='MSFT', padx=9, pady=5, command=microsoft.get_stock)
microsoft_button.grid(row=3, column=4)
meta = Assets('META')
meta_button = Button(main_window, text='META', padx=8, pady=5, command=meta.get_stock)
meta_button.grid(row=4, column=4)


# For Cryptocurrency
bitcoin = Assets('BTC/USD')
btc_button = Button(main_window, text='BTC/USD', padx=4, pady=5, command=bitcoin.get_crypto)
btc_button.grid(row=1, column=7)
ethereum = Assets('ETH/USD')
eth_button = Button(main_window, text='ETH/USD', padx=4, pady=5, command=ethereum.get_crypto)
eth_button.grid(row=2, column=7)

main_window.mainloop()
