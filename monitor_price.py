import requests
from bs4 import BeautifulSoup
import time

def get_latest_sell_order():
    url = "https://www.binance.com/en/orderbook/USDT_VAI"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        sell_orders = soup.select('#sellOrders tbody tr')
        
        if sell_orders:
            latest_sell_order = sell_orders[0]
            price_vai = latest_sell_order.find('td', class_='price').get_text(strip=True)
            amount_usdt = latest_sell_order.find('td', class_='amount').get_text(strip=True)
            return price_vai, amount_usdt
    return None, None

def update_readme(price_vai, amount_usdt):
    with open('README.md', 'w') as readme_file:
        readme_file.write(f"## Latest Sell Order\n\n")
        readme_file.write(f"**Price (VAI)**: {price_vai}\n")
        readme_file.write(f"**Amount (USDT)**: {amount_usdt}\n")

def main():
    while True:
        price_vai, amount_usdt = get_latest_sell_order()
        
        if price_vai is not None and amount_usdt is not None:
            print("Latest Sell Order:")
            print(f"Price (VAI): {price_vai}")
            print(f"Amount (USDT): {amount_usdt}\n")

            update_readme(price_vai, amount_usdt)
        
        time.sleep(300)  # Sleep for 5 minutes

if __name__ == "__main__":
    main()
