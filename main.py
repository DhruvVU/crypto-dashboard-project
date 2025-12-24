from crypto_api import fetch_prices
from database import init_db, save_price, get_last_price
from config import THRESHOLD
from notifications import send_telegram_alert
import schedule
import time

def run():
    #print("1. Program Started.")

    print("------Starting Price Check------")
    init_db()

    curr_prices = fetch_prices()
    if not curr_prices:
        print("Failed to fetch prices")
        return
   
    for symbol, new_price in curr_prices.items():
        old_price = get_last_price(symbol)

        if old_price:
            price_change = (new_price - old_price) / old_price
            percent = f"{price_change * 100:.2f}"

            print(f"{symbol.upper()}: Old=${old_price} -> New=${new_price} ({percent})")

            if price_change <= -THRESHOLD:
                print(f" 🚨 ALERT: {symbol} dropped by {percent}!")
                msg = f"🚨 ALERT: {symbol.upper()} Crash!\nPrice: ${new_price}\nChange:{percent}"
                send_telegram_alert(msg)

            elif price_change >= THRESHOLD:
                print(f" 🚀 MOON: {symbol} went up by {percent}")
                msg = f"🚀 MOON: {symbol} went up by {percent}"
                send_telegram_alert(msg)

            else:
                print(f" No significant change")
        else:
            print(f"{symbol.upper()}: No history found.")

        save_price(symbol, new_price)
    
if __name__ == "__main__":

    print("-----24 Hour Monitor-----")

    run()

    schedule.every(1).hours.do(run)

    while True:
        schedule.run_pending()
        time.sleep(1)

# prices = fetch_prices()

#     if prices : 
#      #   print("5. Saving price to Database.")

#         for symbol, price in prices.items():
#             print(f"Saving {symbol}: {price}")
#             save_price(symbol, price)

#         print("Data saved successfully.")
        
#     else : 
#         print("Failed to fetch prices.")
