# endpoint

An IPC endpoint library for communicating with the plugml engine.

## Installation
### From Releases
`pip install <wheel-file>`
### From Source
clone the repo
```
pip install wheel
python setup.py sdist
python setup.py bdist_wheel
python setup.py build
python setup.py install
```
this will create a wheel file to pip install

## Usage
- `connect(port)`: connect to the plugml engine via a given port
- transmitting data
  - `transmit(data)`: transmit a string to the plugml engine
  - `transmit_list(data)`: transmit a list to the plugml engine
- retrieving data
  - `retrieve()`: blocks until retrieves data from the plugml engine
  - `retrieve_list()`: blocks until retrieves data list from the plugml engine
  - `retrieve_mapped_list()`: blocks until retrieves data list from the plugml engine and performs a mapping function over the data
