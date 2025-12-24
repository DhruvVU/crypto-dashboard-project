import requests
import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message):
    """
    Generate a message for your telegram account
    """

    if not TOKEN or not CHAT_ID:
        print("Error: Telegram essesntials missing in .env!")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id" : CHAT_ID,
        "text" : message
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram Alert sent!")
        else:
            print(f"❌ Failed to send Telegram alert: {response.text}")

    except Exception as e:
        print(f"Error sending alert :{e}!") 