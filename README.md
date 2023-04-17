# PyTeal Starter Kit

Welcome to the PyTeal Starter Kit! This repository provides you with the necessary starter code to begin writing Algorand TEAL smart contract applications using PyTeal. PyTeal is a Python library that allows you to write TEAL programs using Python syntax. With this starter kit, you'll be able to compile your decentralized application (dApp) and generate TEAL approve and clear byte code, which can be exported as strings in a TypeScript file for use with TypeScript.

## Getting Started

### Prerequisites

Before starting, ensure that you have Python 3.x installed on your system. You can check your Python version by running the following command in your terminal:

```python
python3 --version
```

## Installation

To install PyTeal, open your terminal and run the following command:

``sh
pip3 install pyteal
```

This command will install the PyTeal library on your system.

## Usage

1. Clone this repository to your local machine:
```sh
git clone https://github.com/mangoplane/PyTealStarter.git
```

2. Navigate to the directory
```sh
cd PyTealStarter
```

3. Write your dApp using PyTeal by editing the `starterPyTeal.py` file. You can use the provided example code as a starting point.

4. Compile your dApp by running the following command in the terminal:
```sh 
python3 starterPyTeal.py
```

This command will generate TEAL approve and clear byte code that can be used in your Algorand smart contract application. The byte code will also be exported as strings in a TypeScript file (`source.ts`) for use with TypeScript.


## License

This PyTeal Starter Kit is provided under the MIT License. There are no warranties or liabilities associated with using this starter kit. Please use it as is.


## Resources

For more information about PyTeal and Algorand, visit the following resources:

- [PyTeal GitHub Repository](https://github.com/algorand/pyteal)
- [PyTeal Documentation](https://pyteal.readthedocs.io/en/latest/)
- [Algorand Developer Portal](https://developer.algorand.org/)
- [TEAL Language Reference](https://developer.algorand.org/docs/reference/teal/specification/)
