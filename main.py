import requests

import pandas as pd

BINANCE = "https://api.binance.com/api/v3"

def get_klines(symbol="BTCUSDT", interval="15m", limit=200):

    url = f"{BINANCE}/klines"

    params = {"symbol": symbol, "interval": interval, "limit": limit}

    data = requests.get(url, params=params).json()

    df = pd.DataFrame(data, columns=[

        "time","open","high","low","close","volume",

        "c1","c2","c3","c4","c5","c6"

    ])

    df["close"] = df["close"].astype(float)

    return df

def rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0).rolling(period).mean()

    loss = -delta.clip(upper=0).rolling(period).mean()

    rs = gain / loss

    return 100 - (100 / (1 + rs))

def ema(series, period):

    return series.ewm(span=period).mean()

def analyze(df):

    df["rsi"] = rsi(df["close"])

    df["ema50"] = ema(df["close"], 50)

    df["ema200"] = ema(df["close"], 200)

    last = df.iloc[-1]

    trend_up = last["ema50"] > last["ema200"]

    trend_down = last["ema50"] < last["ema200"]

    rsi_val = last["rsi"]

    signal = "NONE"

    if rsi_val < 30 and trend_up:

        signal = "BUY"

    elif rsi_val > 70 and trend_down:

        signal = "SELL"

    print("Phoenix Trader PRO Running...")

    print("RSI:", round(rsi_val, 2))

    print("Trend UP:", trend_up)

    print("Trend DOWN:", trend_down)

    print("SIGNAL:", signal)

df = get_klines("BTCUSDT", "15m")

analyze(df)
