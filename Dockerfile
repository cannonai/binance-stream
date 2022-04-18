FROM python:3.8

COPY . /binance-stream

RUN pip3 install /binance-stream/

ENV BINANCE_STREAM_CONFIG /binance-stream/examples/config.trades.gin

ENTRYPOINT [ "bash", "/binance-stream/entrypoint.sh" ]
