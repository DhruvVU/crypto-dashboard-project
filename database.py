import sqlite3
import datetime

DB_NAME = 'price_history.db'

def init_db():
    with sqlite3.connect(DB_NAME):

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS crypto_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                price REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()

def save_price(symbol, price):

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO crypto_history (symbol, price)
            VALUES (?, ?)
        ''', (symbol, price))
        
        conn.commit()

def get_last_price(symbol):
    """
    Retrieves the most recent price entry for a specific symbol.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT price FROM crypto_history
            WHERE symbol = ?
            ORDER BY timestamp DESC
            LIMIT 1
        ''', (symbol,))
        
        row = cursor.fetchone()
        
        if row:
            return row[0]  # Return the price value 
        else:
            return None    # Return None if this is the first time running