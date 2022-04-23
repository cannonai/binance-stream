# %%
import sys
import os

import gin
import click
from binance.websocket.spot.websocket_client import SpotWebsocketClient as WebsocketClient

from binance_stream import handlers, utils

# %%
sys.path.append(os.getcwd())

# %%
def start_stream(stream, symbols, handler):
    ws_client = WebsocketClient()
    m = 500 # subscribe rate
    for i in range(len(symbols) % m):
        stream_list = [f'{symbol}@{stream}' for symbol in symbols][(i*m):((i+1)*m)]
        ws_client.instant_subscribe(stream=stream_list, callback=handler)
        #time.sleep(0.5)
    ws_client.start()

# %%
@gin.configurable()
def stream(stream='trade', symbols=None, handler=handlers.PrintHandler(), **kwargs):
    if symbols is None:
        symbols = utils.get_trading_symbols()
    
    # start stream
    start_stream(stream, symbols, handler, **kwargs)

# %%
@click.command()
@click.option('--config', default=None)
def main(config):
    if config is not None:
        gin.parse_config_file(config)
    stream()
    
# %%
if __name__ == '__main__':
    main()