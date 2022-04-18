# %%
from setuptools import setup, find_packages

# %%
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

# %%
setup(name='binance_stream',
      version='0.2.0',
      description='CLI for Binance Stream API',
      url='http://github.com/cannonai/bianance-stream',
      author='Marc Horlacher',
      author_email='marc.horlacher@gmail.com',
      license='MIT',
      install_requires=requirements,
      packages=find_packages(),
      include_package_data=True,
      entry_points = {
            'console_scripts': [
                  'binance-stream=binance_stream.__main__:main',
            ],
      },
      zip_safe=False)
