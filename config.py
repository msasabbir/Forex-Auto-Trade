# ===================================
#   📈 Forex Auto Trade Bot
#   config.py — সব settings এখানে
# ===================================

import os
from dotenv import load_dotenv

# .env ফাইল লোড করো
load_dotenv()

# ===== Telegram =====
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
PREMIUM_CHANNEL_ID = os.getenv("PREMIUM_CHANNEL_ID")

# ===== API Keys =====
TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "mistralai/mistral-7b-instruct:free"
)

# ===== Database =====
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///forex_auto_trade.db")

# ===== Forex Pairs =====
FOREX_PAIRS = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "XAU/USD",
    "USD/CAD",
    "AUD/USD"
]

# ===== Signal Schedule (UTC) =====
SIGNAL_TIMES = ["08:00", "12:00", "16:00", "20:00"]

# ===== Free User Limit =====
FREE_SIGNALS_PER_DAY = 2

# ===== Subscription Prices =====
MONTHLY_PRICE = 499
YEARLY_PRICE = 3999

# ===== Required Variables Check =====
REQUIRED_VARS = {
    "BOT_TOKEN": BOT_TOKEN,
    "TWELVEDATA_API_KEY": TWELVEDATA_API_KEY,
    "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
    "ADMIN_ID": ADMIN_ID,
}

for var_name, var_value in REQUIRED_VARS.items():
    if not var_value:
        raise ValueError(
            f"❌ Missing required environment variable: {var_name}\n"
            f"   .env ফাইলে {var_name} সেট করো!"
        )

print("✅ Config loaded successfully!")