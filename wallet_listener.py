from web3.providers.eth_tester import EthereumTesterProvider
from web3 import Web3
from eth_tester import PyEVMBackend

w3 = Web3(EthereumTesterProvider(PyEVMBackend()))

result = w3.eth.get_balance('0xddfAbCdc4D8FfC6d5beaf154f18B778f892A0740')
print(result)