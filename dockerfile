# 1. Download version of linux with python already installed
FROM python:3.11-slim

# 2. Folder created inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Copy rest of code
COPY . .

# Grant permission to run the script
RUN chmod +x entrypoint.sh

EXPOSE 8501

# 6. Run the bot
CMD ["./entrypoint.sh"]