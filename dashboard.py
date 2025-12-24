import pandas as pd
import sqlite3
import streamlit as st
import time

st.set_page_config(page_title='Crypto Project', layout='wide')
st.title("🚀 Live Crypto Dashboard")

def load_data():
    conn = sqlite3.connect('price_history.db')
    df = pd.read_sql("SELECT * FROM crypto_history ORDER BY timestamp DESC", conn)
    conn.close()
    return df

placeholder = st.empty()

while True:
    try:
        df = load_data()

        with placeholder.container():
            if not df.empty:
                col1, col2 = st.columns(2)

                # Bitcoin data chart and table code here
                with col1:
                    st.markdown("🟠 Bitcoin (BTC)")
                    btc_data = df[df['symbol'] == 'bitcoin']

                    if not btc_data.empty:
                        price = btc_data.iloc[0]['price']
                        st.metric("Price", f"{price:.2f}INR")

                        # Bitcoin Chart 
                        chart_data = btc_data.set_index('timestamp')[['price']]
                        st.line_chart(chart_data)

                        # Bitcoin Table
                        st.caption("Recent Bitcoin logs")
                        st.dataframe(btc_data.head(5), width='content')
                    else:
                        st.warning("Waiting for Bitcoin data")

                # Ethereum data chart and table code here
                with col2:
                    st.markdown("🔵 Ethereum (ETH)")
                    eth_data = df[df['symbol'] == 'ethereum']

                    if not eth_data.empty:
                        price = eth_data.iloc[0]['price']
                        st.metric("Price", f"{price:.2f}INR")

                        # Ethereum Chart
                        chart_data = eth_data.set_index('timestamp')[['price']]
                        st.line_chart(chart_data) 

                        # Ethereum Table
                        st.caption("Recent Ethereum logs")
                        st.dataframe(eth_data.head(5), width='content')
                    else:
                        st.warning("Waiting for Ethereum data")

            else:
                st.warning("Database is empty. Waiting for bot to write data...")
        
    except Exception as e:
        st.error("Error reading data: {e}")
    
    time.sleep(2)