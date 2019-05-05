import json
import vns_web3
from vns_web3 import We3,HTTPProvider
import rlp
from solc import compile_source
from web3.contract  import ConciseContract
web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def constract(flap_contract,address_dai,address_gem,from_address,unlock_key):
    address_dai = web3.toChecksumAddress(address_dai)
    address_gem = web3.toChecksumAddress(address_gem)
    
    from_address = web3.toChecksumAddress(from_address)
    ret = web3.personal.unlockAccount(account=from_address,passphrase=unlock_key)
    
    txid = flap_contract.constructor(address_dai,address_gem).transact({'from': from_address})
    
    tx_data = web3.vns.waitForTransactionReceipt(txid)
    web3.personal.lockaccount(account=from_address)
    return tx_data

def printAllFunc(flap_contract):
    all_func = flap_contract.all_functions()
    print(all_func)
