# ===================================
#   📈 Forex Auto Trade Bot
#   fetcher.py — Market Data Fetcher
# ===================================

import requests
import pandas as pd
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import TWELVEDATA_API_KEY

BASE_URL = "https://api.twelvedata.com"

def get_price_data(
    symbol: str,
    interval: str = "1h",
    outputsize: int = 100
) -> pd.DataFrame:
    """
    Twelve Data API থেকে OHLCV ডেটা আনো।
    
    Args:
        symbol: Forex pair যেমন "EUR/USD"
        interval: টাইমফ্রেম — "15min", "1h", "4h", "1day"
        outputsize: কতটি candle আনবে (max 5000)
    
    Returns:
        pandas DataFrame (open, high, low, close, volume)
    """
    url = f"{BASE_URL}/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": TWELVEDATA_API_KEY,
        "format": "JSON"
    }

    # ৩ বার চেষ্টা করো (retry logic)
    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            # API error চেক
            if data.get("status") == "error":
                print(f"⚠️ API Error: {data.get('message')}")
                return pd.DataFrame()

            values = data.get("values", [])
            if not values:
                print(f"⚠️ No data returned for {symbol}")
                return pd.DataFrame()

            # DataFrame বানাও
            df = pd.DataFrame(values)
            df = df.rename(columns={"datetime": "time"})

            # সব price column কে float এ convert করো
            for col in ["open", "high", "low", "close"]:
                df[col] = df[col].astype(float)

            # পুরনো থেকে নতুন ক্রমে সাজাও
            df = df.iloc[::-1].reset_index(drop=True)

            return df

        except requests.exceptions.Timeout:
            print(f"⏱️ Timeout! চেষ্টা {attempt + 1}/3")
            time.sleep(2)

        except requests.exceptions.ConnectionError:
            print(f"🌐 Connection Error! চেষ্টা {attempt + 1}/3")
            time.sleep(3)

        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return pd.DataFrame()

    print(f"❌ {symbol} এর ডেটা আনা সম্ভব হয়নি!")
    return pd.DataFrame()


def get_current_price(symbol: str) -> float:
    """
    একটি পেয়ারের বর্তমান মূল্য আনো।
    
    Returns:
        float: current price, অথবা 0.0 যদি error হয়
    """
    url = f"{BASE_URL}/price"
    params = {
        "symbol": symbol,
        "apikey": TWELVEDATA_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        return float(data.get("price", 0.0))

    except Exception as e:
        print(f"❌ Price fetch error for {symbol}: {e}")
        return 0.0