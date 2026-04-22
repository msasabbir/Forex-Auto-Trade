# ===================================
#   📈 Forex Auto Trade Bot
#   indicators.py — Technical Analysis
# ===================================

import pandas as pd
import ta


def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    সব টেকনিক্যাল ইন্ডিকেটর ক্যালকুলেট করো।
    
    Indicators:
        - RSI (Relative Strength Index)
        - MACD (Moving Average Convergence Divergence)
        - EMA 20, 50, 200 (Exponential Moving Average)
        - Bollinger Bands
        - ATR (Average True Range)
        - Stochastic Oscillator
    
    Args:
        df: OHLCV DataFrame (fetcher.py থেকে আসা)
    
    Returns:
        DataFrame with all indicator columns added
    """

    if df.empty or len(df) < 50:
        print("⚠️ পর্যাপ্ত ডেটা নেই indicators এর জন্য!")
        return df

    close = df["close"]
    high = df["high"]
    low = df["low"]

    # ===== RSI =====
    # ৩০ এর নিচে = Oversold (কেনার সুযোগ)
    # ৭০ এর উপরে = Overbought (বেচার সুযোগ)
    df["rsi"] = ta.momentum.RSIIndicator(
        close=close, window=14
    ).rsi()

    # ===== MACD =====
    # MACD > Signal = Bullish (upward momentum)
    # MACD < Signal = Bearish (downward momentum)
    macd_indicator = ta.trend.MACD(close=close)
    df["macd"] = macd_indicator.macd()
    df["macd_signal"] = macd_indicator.macd_signal()
    df["macd_diff"] = macd_indicator.macd_diff()

    # ===== EMA (Exponential Moving Average) =====
    # EMA20 > EMA50 = Short-term uptrend
    # EMA50 > EMA200 = Long-term uptrend
    df["ema_20"] = ta.trend.EMAIndicator(
        close=close, window=20
    ).ema_indicator()

    df["ema_50"] = ta.trend.EMAIndicator(
        close=close, window=50
    ).ema_indicator()

    df["ema_200"] = ta.trend.EMAIndicator(
        close=close, window=200
    ).ema_indicator()

    # ===== Bollinger Bands =====
    # Price near lower band = Oversold (buy zone)
    # Price near upper band = Overbought (sell zone)
    bb = ta.volatility.BollingerBands(close=close, window=20)
    df["bb_upper"] = bb.bollinger_hband()
    df["bb_middle"] = bb.bollinger_mavg()
    df["bb_lower"] = bb.bollinger_lband()

    # ===== ATR (Average True Range) =====
    # Volatility measure — বড় ATR = বেশি volatile market
    df["atr"] = ta.volatility.AverageTrueRange(
        high=high, low=low, close=close, window=14
    ).average_true_range()

    # ===== Stochastic Oscillator =====
    # K < 20 = Oversold, K > 80 = Overbought
    stoch = ta.momentum.StochasticOscillator(
        high=high, low=low, close=close
    )
    df["stoch_k"] = stoch.stoch()
    df["stoch_d"] = stoch.stoch_signal()

    # NaN rows বাদ দাও
    df = df.dropna().reset_index(drop=True)

    return df