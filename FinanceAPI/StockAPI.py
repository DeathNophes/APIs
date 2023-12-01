import requests
key = ''

"""
You need to create a registration at https://twelvedata.com/ to get a unique APIkey
"""


def get_asset(symbol):
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={key}"
    try:
        request = requests.get(url)
        data = request.json()

        print(f"Stock: {data['meta']['symbol']}\n"
              f"-Current price (USD): {data['values'][0]['close']}\n"
              f"-Last refreshed: {data['values'][0]['datetime']}")

    except requests.exceptions.RequestException as e:
        print('Error'), e


stock_name = input()  # Enter valid symbols or else the program will crash

get_asset(stock_name)

"""
Example output:
Stock: GOOGL
-Current price (USD): 131.77499
-Last refreshed: 2023-11-30 12:51:00
"""