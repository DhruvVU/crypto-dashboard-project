# 1. Download version of linux with python already installed
FROM python:3.9-slim

# 2. Folder created inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 


# 5. Copy rest of code
COPY . .

# 6. Run the bot
CMD ["python", "-u","main.py"]