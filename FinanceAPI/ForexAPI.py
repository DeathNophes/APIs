import requests
key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


def get_forex_pair(symbol):
    url = f"https://api.twelvedata.com/exchange_rate?symbol={symbol}&apikey={key}"
    try:
        request = requests.get(url)
        data = request.json()

        if 'status' in data.keys():
            print('Error!')
            exit()

        print(f"{data['symbol']} -> {data['rate']}")

    except requests.exceptions.RequestException as e:
        print('Error'), e


pair = input()
get_forex_pair(pair)

"""
Example output:
EUR/USD -> 1.0887
"""
