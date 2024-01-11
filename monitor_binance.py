import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime
from pytz import timezone

load_dotenv()

# Binance URL for the order book
binance_url = "https://www.binance.com/en/orderbook/USDT_VAI"

# Define the IST timezone
ist = timezone('Asia/Kolkata')

def update_readme(message):
    # Get the current time in IST
    current_time = datetime.now(ist)
    # Format the time as HH:mm AM/PM
    formatted_time = current_time.strftime('%I:%M %p')

    with open('README.md', 'a') as f:
        f.write(f"{formatted_time} - {message}\n")

def monitor_binance_order_book():
    response = requests.get(binance_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract sell orders
    sell_orders = soup.select('.sellOrderWrapper tbody tr')

    price_hit = False
    for order in sell_orders:
        price = float(order.select_one('.price').text.strip())
        if price <= 1.000:
            notification_message = f"Price Alert! Sell order price reached or went below 1.000 VAI\nPrice: {price}"
            update_readme(notification_message)
            price_hit = True
            break  # Stop checking further once the condition is met

    if not price_hit:
        update_readme("Didn't hit the target price in this check.")

if __name__ == "__main__":
    monitor_binance_order_book()
