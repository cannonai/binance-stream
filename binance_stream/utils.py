# %%
import sys

from binance.spot import Spot as Client
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

# %%
def get_trading_symbols():
    client = Client()
    info = client.exchange_info()
    return [symbol['symbol'].lower() for symbol in info['symbols'] if symbol['status'] == 'TRADING']
