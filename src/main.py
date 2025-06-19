"""
A simple real-time stock price monitor simulation.
"""
import random
import time

def get_stock_price(symbol: str) -> float:
    """
    Simulate fetching a real-time stock price (mocked).
    """
    return round(100 + random.uniform(-5, 5), 2)

def monitor_stock(symbol: str, threshold: float, interval: int = 2, checks: int = 5):
    """
    Monitor the stock price and print an alert if it exceeds the threshold.
    """
    print(f"Monitoring {symbol} for price above {threshold}...")
    for _ in range(checks):
        price = get_stock_price(symbol)
        print(f"Current price of {symbol}: ${price}")
        if price > threshold:
            print(f"ALERT: {symbol} price above threshold! (${price} > ${threshold})")
        time.sleep(interval)

if __name__ == "__main__":
    monitor_stock("AAPL", threshold=103.0)
