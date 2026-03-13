# Build-a-Simplified-Trading-Bot-Binance-Futures-Testnet-
A small Python application that can place orders on Binance Futures Testnet (USDT-M) and provide a clean, reusable structure with proper logging and error handling.
Trading Bot – Binance Futures Testnet
Setup

- Install dependencies:
pip install -r requirements.txt

- Set environment variables:
export BINANCE_API_KEY="your_testnet_api_key"
export BINANCE_API_SECRET="your_testnet_api_secret"

- Place a MARKET order:
python cli.py order BTCUSDT BUY MARKET 0.01

- Place a LIMIT order:
python cli.py order BTCUSDT SELL LIMIT 0.01 --price 60000

- Place a STOP_LIMIT order (bonus):
python cli.py order BTCUSDT SELL STOP_LIMIT 0.01 --price 58000

- Whenever you run a command like
python cli.py order BTCUSDT BUY MARKET 0.002
