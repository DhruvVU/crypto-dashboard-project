import requests
from config import API_URL, COINS, CURRENCY

def fetch_prices():
    params = {
        'ids': COINS,
        'vs_currencies': CURRENCY
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Simplify the data structure
        return {
            'bitcoin': data['bitcoin'][CURRENCY],
            'ethereum': data['ethereum'][CURRENCY]
        }
    except Exception as e:
        print(f"API Error: {e}")
        return None 