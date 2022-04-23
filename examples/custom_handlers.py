import gin

# %%
@gin.register()
class CustomPrintHandler():
    def __init__(self) -> None:
        pass
    
    def __call__(self, msg):
        print(f'Custom handler yields: {msg}')