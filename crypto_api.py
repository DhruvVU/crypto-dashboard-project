import requests
import config

def fetch_prices():
    currency = config.CURRENCY.upper()
    btc_url = f"https://api.coinbase.com/v2/prices/BTC-{currency}/spot"
    eth_url = f"https://api.coinbase.com/v2/prices/ETH-{currency}/spot"

    try:
        prices = {}

        # Fetch bitcoin
        response_btc = requests.get(btc_url)
        if response_btc.status_code == 200:
            data = response_btc.json()
            prices['bitcoin'] = float(data['data']['amount'])
        else:
            print(f"⚠️ Failed to fetch BTC: {response_btc.status_code}")

        # Fetch ethereum
        response_eth = requests.get(eth_url)
        if response_eth.status_code == 200:
            data = response_eth.json()
            prices['ethereum'] = float(data['data']['amount'])
        else:
            print(f"⚠️ Failed to fetch ETH: {response_eth.status_code}")

        if prices:
            return prices
        else:
            return None

    except Exception as e:
        print(f"API Error: {e}")
        return None 