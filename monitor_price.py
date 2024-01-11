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
            order_data = [td.get_text(strip=True) for td in latest_sell_order.find_all('td')]
            return order_data
    return None

def main():
    while True:
        latest_sell_order = get_latest_sell_order()
        
        if latest_sell_order:
            print("Latest Sell Order:")
            print(f"Order: {latest_sell_order[0]}")
            print(f"Side: {latest_sell_order[1]}")
            print(f"Price (VAI): {latest_sell_order[2]}")
            print(f"Amount (USDT): {latest_sell_order[3]}")
            print(f"Total (VAI): {latest_sell_order[4]}")
            print(f"Sum (VAI): {latest_sell_order[5]}")
            print("\n")
        
        time.sleep(300)  # Sleep for 5 minutes

if __name__ == "__main__":
    main()
