print("Phoenix Trader is running...")
import requests

def get_price(symbol="BTCUSDT"):

    url = "https://api.binance.com/api/v3/ticker/price"

    r = requests.get(url, params={"symbol": symbol})

    return float(r.json()["price"])

price = get_price()

print("BTC Price:", price)
