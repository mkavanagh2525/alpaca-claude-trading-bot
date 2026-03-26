import os
import sys
from datetime import datetime
import pytz
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("=== Alpaca Claude Trading Bot Started ===")
print(f"Time: {datetime.now(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Python version: {sys.version}")

# Basic Alpaca setup check
api_key = os.getenv("APCA_API_KEY_ID")
secret_key = os.getenv("APCA_API_SECRET_KEY")
base_url = os.getenv("APCA_API_BASE_URL")

print(f"API Key ID loaded: {'Yes' if api_key else 'No'}")
print(f"Base URL: {base_url or 'Not set'}")

if not api_key or not secret_key:
    print("ERROR: Alpaca API keys not found in environment variables!")
    print("Please add APCA_API_KEY_ID, APCA_API_SECRET_KEY, and APCA_API_BASE_URL in Railway Variables.")
    sys.exit(1)

print("Alpaca credentials detected. Ready for trading logic.")

# =============================================
# SIMPLE STRATEGY - RSI Mean Reversion on SPY
# =============================================

try:
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    from alpaca.trading.client import TradingClient
    from alpaca.trading.requests import MarketOrderRequest
    from alpaca.trading.enums import OrderSide, TimeInForce

    print("Alpaca libraries imported successfully.")

    # Initialize clients
    trading_client = TradingClient(api_key, secret_key, paper=True)
    data_client = StockHistoricalDataClient(api_key, secret_key)

    # Get account info
    account = trading_client.get_account()
    print(f"Account Equity: ${float(account.equity):.2f}")
    print(f"Buying Power: ${float(account.buying_power):.2f}")

    # Simple check: Is market open?
    clock = trading_client.get_clock()
    print(f"Market is {'OPEN' if clock.is_open else 'CLOSED'}")

    if not clock.is_open:
        print("Market is closed. No trades today.")
    else:
        print("Market is open. Running strategy check...")

        # Basic RSI logic placeholder (you can expand this)
        print("Strategy check complete. No trade signal triggered in this version.")

except Exception as e:
    print(f"ERROR during execution: {e}")
    import traceback
    traceback.print_exc()

print("=== Bot execution finished ===")
