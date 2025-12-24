import requests
from config import API_URL, COINS, CURRENCY

def fetch_prices():
    params = {
        'ids': COINS,
        'vs_currencies': CURRENCY
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(API_URL, params=params, headers=headers, timeout=10)

        if response.status_code == 429:
            print("⚠️ Rate Limit Hit (429). Skipping this check.")
            return None
        
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