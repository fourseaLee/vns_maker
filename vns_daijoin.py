import json
import vns_web3
from vns_web3 import We3,HTTPProvider
import rlp
from solc import compile_source
from web3.contract  import ConciseContract
web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def constractGem(gem_contract,address_vat,bytecode32_ilk,from_address,unlock_key):
    address_vat = web3.toChecksumAddress(address_vat)

    from_address = web3.toChecksumAddress(from_address)
    ret = web3.personal.unlockAccount(account=from_address,passphrase=unlock_key)
    
    txid = gem_contract.constructor(address_vat,bytecode32_ilk).transact({'from': from_address})
    
    tx_data = web3.vns.waitForTransactionReceipt(txid)
    web3.personal.lockaccount(account=from_address)
    return tx_data

def printGemAllFunc(gem_contract):
    all_func = gem_contract.all_functions()
    print(all_func)

def constractVns(vns_contract,address_vat,bytecode32_ilk,from_address,unlock_key):
    address_vat = web3.toChecksumAddress(address_vat)

    from_address = web3.toChecksumAddress(from_address)
    ret = web3.personal.unlockAccount(account=from_address,passphrase=unlock_key)
    
    txid = gem_contract.constructor(address_vat,bytecode32_ilk).transact({'from': from_address})
    
    tx_data = web3.vns.waitForTransactionReceipt(txid)
    web3.personal.lockaccount(account=from_address)
    return tx_data

def printVnsAllFunc(vns_contract):
    all_func = vns_contract.all_functions()
    print(all_func)

def constractDai(dai_contract,address_vat,address_dai,from_address,unlock_key):
    address_vat = web3.toChecksumAddress(address_vat)
    address_dai = web3.toChecksumAddress(address_dai)

    from_address = web3.toChecksumAddress(from_address)
    ret = web3.personal.unlockAccount(account=from_address,passphrase=unlock_key)
    
    txid = gem_contract.constructor(address_vat,address_dai).transact({'from': from_address})
    
    tx_data = web3.vns.waitForTransactionReceipt(txid)
    web3.personal.lockaccount(account=from_address)
    return tx_data

def printDaiAllFunc(dai_contract):
    all_func = dai_contract.all_functions()
    print(all_func)   
