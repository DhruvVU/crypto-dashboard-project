import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

print(f"--- DEBUG INFO ---")
print(f"My Token is: '{TOKEN}'") # Single quotes help us see accidental spaces
print(f"------------------")

if TOKEN:
    URL = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(URL)
    print(response.json())
else:
    print("ERROR: Token is Empty! Check your .env file.")