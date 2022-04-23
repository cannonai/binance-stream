# binance-stream

## Install

```
pip install git+https://github.com/cannonai/binance-stream.git
```

## Quickstart

### Basic Usage

```
binance-stream --config config.gin
```


### Defining a `config.gin` File

The config file gives control over streaming endpoints, trading pairs and message handlers. 
The following configuration will access the `trades` endpoint and stream events from the `btcusdt` and `ethusdt` pairs. 

```
stream.stream = 'trade'
stream.symbols = ['btcusdt', 'ethusdt']
```

For more examples, see `examples/`.


### Using Custom Handlers

Handlers define how stream messages are processed. A few handlers are packages with binance-stream, including the `PrintHandler` and `FileHandler`. 
One may also define custom handlers and import them directly into the config file to be used by binance-stream at runtime. A minimal example is shown below. 

```
git clone https://github.com/cannonai/binance-stream.git && cd binance-stream/examples
```

```
binance-stream --config config.custom_handler.gin
```

File content: `custom_handlers.py`
```
import gin

# %%
@gin.register()
class CustomPrintHandler():
    def __init__(self) -> None:
        pass
    
    def __call__(self, msg):
        print(f'Custom handler yields: {msg}')
```

File content: `config.custom_handler.gin`
```
# import custom handler(s)
import custom_handlers

stream.stream = 'kline_1m'
stream.symbols = ['btcusdt', 'ethusdt']

# set use of custom handler
stream.handler = @custom_handlers.CustomPrintHandler()
```


---

*Version 0.2.0*