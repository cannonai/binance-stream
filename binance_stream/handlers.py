import sys

import gin

# %%
@gin.configurable()
class PrintHandler():
    def __init__(self, out=sys.stderr) -> None:
        self._out = out
    
    def __call__(self, msg):
        print(msg, file=self._out)

# %%
@gin.configurable()
class FileHandler():
    def __init__(self, fname) -> None:
        self._file = open(fname, 'w')
    
    def __call__(self, msg):
        print(msg, file=self._file)

# %%
@gin.configurable()
class KafkaHandler():
    def __init__(self) -> None:
        pass
    
    def __call__(self, msg):
        #kafka_producer.send(topic='binance-trades', value=msg)
        pass