# %%
import click

# %%
from binance_stream.bin import stream

# %%
# @click.group()
# def main():
#     pass

# main.add_command(stream.main, name='stream')

# %%
def main():
    stream.main()

# %%
if __name__ == '__main__':
    main()