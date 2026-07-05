print("Phoenix Trader is running...")
import requests

def get_price(symbol="BTCUSDT"):

    url = "https://api.binance.com/api/v3/ticker/price"

    r = requests.get(url, params={"symbol": symbol})

    return float(r.json()["price"])

price = get_price()

print("BTC Price:", import requests

def get_price(symbol="BTCUSDT"):

    url = "https://api.binance.com/api/v3/ticker/price"

    r = requests.get(url, params={"symbol": symbol})

    return float(r.json()["price"])

def get_rsi(price):

    return 25 if price % 5 == 0 else 55

def get_ema_trend(price):

    return "UP" if price % 2 == 0 else "DOWN"

price = get_price()

rsi = get_rsi(price)

trend = get_ema_trend(price)

signal = "NONE"

if rsi < 30 and trend == "UP":

    signal = "BUY"

elif rsi > 70 and trend == "DOWN":

    signal = "SELL"

print("Phoenix Trader Running...")

print("Price:", price)

print("RSI:", rsi)

print("Trend:", trend)

print("Signal:", signal)
