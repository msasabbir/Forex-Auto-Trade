# 📈 Forex Auto Trade Bot

> Real-time AI-powered Forex Signal Bot for Telegram
> 🤖 [@forexautotrad_bot](https://t.me/forexautotrad_bot)

---

## ✨ Features

- 📊 Real-time Forex Signal (BUY/SELL/HOLD)
- 🤖 AI Market Commentary (OpenRouter)
- 📉 Technical Analysis (RSI, MACD, EMA, BB)
- 💎 Free & Premium Subscription System
- ⏰ Auto Signal every 4 hours
- 🌍 6+ Forex Pairs supported

---

## 📌 Supported Pairs

| Pair      | Name                  |
|-----------|-----------------------|
| EUR/USD   | Euro / US Dollar      |
| GBP/USD   | British Pound / USD   |
| USD/JPY   | US Dollar / Yen       |
| XAU/USD   | Gold / US Dollar      |
| USD/CAD   | US Dollar / CAD       |
| AUD/USD   | Australian Dollar/USD |

---

## 🤖 Bot Commands

| Command         | Description                  |
|-----------------|------------------------------|
| /start          | Welcome message              |
| /signal EURUSD  | Get signal for a pair        |
| /pairs          | Show all available pairs     |
| /subscribe      | View premium plans           |
| /account        | Your subscription status     |
| /admin          | Bot stats (Admin only)       |

---

## 💰 Subscription Plans

| Plan       | Price      | Signals/day |
|------------|------------|-------------|
| Free       | 0৳         | 2           |
| Monthly    | 499৳/month | Unlimited   |
| Yearly     | 3,999৳/yr  | Unlimited   |

---

## 🛠️ Tech Stack

- **Language:** Python 3.11+
- **Bot Library:** python-telegram-bot v20
- **Market Data:** Twelve Data API
- **AI Analysis:** OpenRouter API
- **Database:** SQLite + SQLAlchemy
- **Scheduler:** APScheduler
- **Hosting:** Koyeb (Free)

---

## ⚙️ Setup & Installation

### ১. Clone the repo
\```bash
git clone https://github.com/yourusername/forex-signal-bot.git
cd forex-signal-bot
\```

### ২. Install dependencies
\```bash
pip install -r requirements.txt
\```

### ৩. Setup environment variables
\```bash
cp .env.example .env
# .env ফাইলে তোমার API keys দাও
\```

### ৪. Run the bot
\```bash
python bot/main.py
\```

---

## 🚀 Deploy on Koyeb

1. GitHub এ push করো
2. [koyeb.com](https://koyeb.com) এ যাও
3. New App → GitHub repo select করো
4. Environment variables সেট করো
5. Run command: `python bot/main.py`
6. Deploy! ✅

---

## 📁 Project Structure

\```
forex-signal-bot/
├── bot/
│   ├── main.py
│   ├── handlers.py
│   └── keyboards.py
├── analysis/
│   ├── fetcher.py
│   ├── indicators.py
│   ├── signal_engine.py
│   └── ai_commentary.py
├── database/
│   └── db.py
├── scheduler/
│   └── jobs.py
├── config.py
├── requirements.txt
├── Procfile
├── .env.example
└── README.md
\```

---

## ⚠️ Disclaimer

> This bot is for **educational purposes only**.
> Forex trading involves significant risk.
> Always do your own research before trading.

---

## 👨‍💻 Developer

Made with ❤️ | [@forexautotrad_bot](https://t.me/forexautotrad_bot)
