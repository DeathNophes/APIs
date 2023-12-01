import requests
key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


def get_crypto(symbol):
    url = f"https://api.twelvedata.com/exchange_rate?symbol={symbol}&apikey={key}"
    try:
        request = requests.get(url)
        data = request.json()

        print(f"{data['symbol']} -> {data['rate']}")

    except requests.exceptions.RequestException as e:
        print('Error'), e


pair = input()  # Enter a valid pair or else the program will crash
get_crypto(pair)

"""
Example output:
BTC/USD -> 37739.73
"""