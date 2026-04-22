# ===================================
#   📈 Forex Auto Trade Bot
#   signal_engine.py — Signal Generator
# ===================================

import pandas as pd
from datetime import datetime, timezone


def generate_signal(df: pd.DataFrame, symbol: str) -> dict:
    """
    টেকনিক্যাল ইন্ডিকেটর বিশ্লেষণ করে BUY/SELL/HOLD সিগনাল তৈরি করো।
    
    Scoring System:
        প্রতিটি indicator একটি score দেয়
        পজিটিভ score = BUY সিগনাল
        নেগেটিভ score = SELL সিগনাল
    
    Returns:
        dict: signal, entry, tp1-3, sl, confidence, rsi, trend
    """

    if df.empty:
        return {"signal": "❌ ERROR", "error": "No data available"}

    # সর্বশেষ candle নাও
    latest = df.iloc[-1]
    prev = df.iloc[-2]  # আগের candle (crossover detect করতে)

    score = 0
    reasons = []

    # ===== ১. RSI Analysis =====
    rsi = latest["rsi"]

    if rsi < 35:
        score += 2
        reasons.append(f"RSI {rsi:.1f} — Oversold 📉")
    elif rsi < 45:
        score += 1
        reasons.append(f"RSI {rsi:.1f} — Slightly Oversold")
    elif rsi > 65:
        score -= 2
        reasons.append(f"RSI {rsi:.1f} — Overbought 📈")
    elif rsi > 55:
        score -= 1
        reasons.append(f"RSI {rsi:.1f} — Slightly Overbought")

    # ===== ২. MACD Crossover =====
    # আগে MACD < Signal ছিল, এখন MACD > Signal = Bullish Crossover
    if prev["macd"] < prev["macd_signal"] and \
       latest["macd"] > latest["macd_signal"]:
        score += 2
        reasons.append("MACD Bullish Crossover 🟢")
    elif prev["macd"] > prev["macd_signal"] and \
         latest["macd"] < latest["macd_signal"]:
        score -= 2
        reasons.append("MACD Bearish Crossover 🔴")
    elif latest["macd"] > latest["macd_signal"]:
        score += 1
        reasons.append("MACD Bullish")
    else:
        score -= 1
        reasons.append("MACD Bearish")