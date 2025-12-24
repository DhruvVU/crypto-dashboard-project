#!/bin/bash

# Starting crypto bot in background
echo "Starting Crypto bot..."
python main.py &

# Starting dashboard in foreground
echo "Starting Dashboard..."
streamlit run dashboard.py --server.port $PORT --server.address 0.0.0.0