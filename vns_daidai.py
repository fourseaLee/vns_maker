import json
import vns_web3
from vns_web3 import We3,HTTPProvider
import rlp
from solc import compile_source
from web3.contract  import ConciseContract
web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def constract(dai_contract,symbol,name,version,chainId,from_address,unlock_key):
    from_address = web3.toChecksumAddress(from_address)
    ret = web3.personal.unlockAccount(account=from_address,passphrase=unlock_key)

    txid = dai_contract.constructor(symbol,name,version,chainId).transact({'from': from_address})
    tx_data = web3.vns.waitForTransactionReceipt(txid)
    web3.personal.lockaccount(account=from_address)
    return tx_data

def printAllFunc(dai_contract):
    all_func = dai_contract.all_functions()
    print(all_func)
