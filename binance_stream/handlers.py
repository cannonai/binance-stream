# %%
import sys
import random

import gin

# %%
class BaseHandler():
    def __init__(self) -> None:
        pass
    
    def process_msg(self, msg):
        raise NotImplementedError()
    
    def __call__(self, msg):
        if msg is not None:
            return self.process_msg(msg)

# %%
@gin.configurable()
class PrintHandler(BaseHandler):
    def __init__(self, out=sys.stderr) -> None:
        super().__init__()
        
        self._out = out
    
    def process_msg(self, msg):
        print(msg, file=self._out)

# %%
@gin.configurable()
class FileHandler(BaseHandler):
    def __init__(self, fname) -> None:
        super().__init__()
        
        self._file = open(fname, 'w')
    
    def process_msg(self, msg):
        print(msg, file=self._file)

# %%
@gin.configurable()
class HandlerChain(BaseHandler):
    def __init__(self, handlers) -> None:
        super().__init__()
        
        self._handler_chain = self._make_chain(handlers)
    
    def _make_chain(self, handlers):
        assert isinstance(handlers, list)
        
        def _chain(x):
            for f in [lambda x: x] + handlers:
                x = f(x)
            return x
        return _chain
    
    def process_msg(self, msg):
        return self._handler_chain(msg)

# %%
@gin.configurable()
class DropoutHandler(BaseHandler):
    def __init__(self, dropout_rate=0.5) -> None:
        super().__init__()
        
        self.dropout_rate = dropout_rate
    
    def process_msg(self, msg):
        if random.random() > self.dropout_rate:
            return msg

# %%
import json
from kafka import KafkaProducer

@gin.configurable()
class KafkaHandler(BaseHandler):
    def __init__(self, topic, **kwargs) -> None:
        super().__init__()
        
        self.topic = topic
        self._producer = KafkaProducer(**kwargs, value_serializer = lambda x: json.dumps(x).encode('UTF-8'))
    
    def process_msg(self, msg):
        if msg is None:
            print('IS NONE!!')
        
        self._producer.send(topic=self.topic, value=msg)

# %%
