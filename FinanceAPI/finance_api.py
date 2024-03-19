import requests
from tkinter import Tk, Label, Button

key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


class GetAssetsInfo:
    def __init__(self, symbol):
        self.symbol = symbol

    # Forex pairs
    def get_forex_pair(self):
        url = f"https://api.twelvedata.com/exchange_rate?symbol={self.symbol}&apikey={key}"
        try:
            request = requests.get(url)
            data = request.json()

            print(f"{data['symbol']} -> {data['rate']}")

        except requests.exceptions.RequestException as e:
            print('Error'), e

    # Stocks
    def get_stock_price(self):
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
    def get_crypto_price(self):
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
assets = Label(main_window, text='Stocks')
assets.grid(row=0, column=3, columnspan=3, padx=50, pady=20)
cryptocurrency = Label(main_window, text='Cryptocurrency:')
cryptocurrency.grid(row=0, column=6, columnspan=3, padx=50, pady=50)

"""
Buttons
"""

# For Forex
eur_usd = GetAssetsInfo('EUR/USD')
eur_usd_button = Button(main_window, text='EUR/USD', padx=5, pady=5, command=eur_usd.get_forex_pair)
eur_usd_button.grid(row=1, column=1)
eur_bgn = GetAssetsInfo('EUR/BGN')
eur_bgn_button = Button(main_window, text='EUR/BGN', padx=4, pady=5, command=eur_bgn.get_forex_pair)
eur_bgn_button.grid(row=2, column=1)
usd_jpy = GetAssetsInfo('USD/JPY')
usd_jpy_button = Button(main_window, text='USD/JPY', padx=6, pady=5, command=usd_jpy.get_forex_pair)
usd_jpy_button.grid(row=3, column=1)
usd_rub = GetAssetsInfo('USD/RUB')
usd_rub_button = Button(main_window, text='USD/RUB', padx=5, pady=5, command=usd_rub.get_forex_pair)
usd_rub_button.grid(row=4, column=1)


# For Stocks
apple = GetAssetsInfo('AAPL')
apple_button = Button(main_window, text='APPLE', padx=6, pady=5, command=apple.get_stock_price)
apple_button.grid(row=1, column=4)
google = GetAssetsInfo('GOOGL')
google_button = Button(main_window, text='GOOGL', padx=3, pady=5, command=google.get_stock_price)
google_button.grid(row=2, column=4)
microsoft = GetAssetsInfo('MSFT')
microsoft_button = Button(main_window, text='MSFT', padx=9, pady=5, command=microsoft.get_stock_price)
microsoft_button.grid(row=3, column=4)
meta = GetAssetsInfo('META')
meta_button = Button(main_window, text='META', padx=8, pady=5, command=meta.get_stock_price)
meta_button.grid(row=4, column=4)


# For Cryptocurrency
bitcoin = GetAssetsInfo('BTC/USD')
btc_button = Button(main_window, text='BTC/USD', padx=4, pady=5, command=bitcoin.get_crypto_price)
btc_button.grid(row=1, column=7)
ethereum = GetAssetsInfo('ETH/USD')
eth_button = Button(main_window, text='ETH/USD', padx=4, pady=5, command=ethereum.get_crypto_price)
eth_button.grid(row=2, column=7)

main_window.mainloop()
