import json
import vns_web3
from vns_web3 import Web3, HTTPProvider
import rlp
from solc import compile_source
from web3.contract import ConciseContract
web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def getCat(contract_address):
    json_file = open('dss/output/Cat.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)
    
    cat = web3.vns.contract(address=contract_address, abi=json_abi)
    return cat


def getDai(contract_address):
    json_file = open('dss/output/Dai.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    dai = web3.vns.contract(address=contract_address, abi=json_abi)
    return dai
    

def getDaiJoin(contract_address):
    json_file = open('dss/output/DaiJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    dai_join = web3.vns.contract(address=contract_address, abi=json_abi)
    return dai_join


def getDSNote(contract_address):
    json_file = open('dss/output/DSNote.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    dsnote = web3.vns.contract(address=contract_address, abi=json_abi)
    return dsnote


def getDSTokenLike(contract_address):
    json_file = open('dss/output/DSTokenLike.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    dstoken_like = web3.vns.contract(address=contract_address, abi=json_abi)
    return dstoken_like


def getETHJoin(contract_address):
    json_file = open('dss/output/ETHJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    eth_join = web3.vns.contract(address=contract_address, abi=json_abi)
    return eth_join
    

def getFlapper(contract_address):
    json_file = open('dss/output/Flapper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    flapper = web3.vns.contract(address=contract_address, abi=json_abi)
    return flapper


def getFlippy(contract_address):
    json_file = open('dss/output/Flippy.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    flippy = web3.vns.contract(address=contract_address, abi=json_abi)
    return flippy
    

def getFlipper(contract_address):
    json_file = open('dss/output/Flipper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    flipper = web3.vns.contract(address=contract_address, abi=json_abi)
    return flipper


def getFlopper(contract_address):
    json_file = open('dss/output/Flopper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    flopper = web3.vns.contract(address=contract_address, abi=json_abi)
    return flopper
    

def getFusspot(contract_address):
    json_file = open('dss/output/Fusspot.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    fusspot = web3.vns.contract(address=contract_address, abi=json_abi)
    return fusspot


def getGemJoin(contract_address):
    json_file = open('dss/output/GemJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    gem_join = web3.vns.contract(address=contract_address, abi=json_abi)
    return gem_join


def getHopeful(contract_address):
    json_file = open('dss/output/Hopeful.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    hopeful = web3.vns.contract(address=contract_address, abi=json_abi)
    return hopeful


def getJug(contract_address):
    json_file = open('dss/output/Jug.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    print(json_abi)

    contract_address = web3.toChecksumAddress(contract_address)

    jug = web3.vns.contract(address=contract_address, abi=json_abi)
    return jug
    

def getVat(contract_address):
    json_file = open('dss/output/Vat.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    vat = web3.vns.contract(address=contract_address, abi=json_abi)
    return vat


def getVow(contract_address):
    json_file = open('dss/output/Vow.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    vow = web3.vns.contract(address=contract_address, abi=json_abi)
    return vow
    

def getVowLike(contract_address):
    json_file = open('dss/output/VowLike.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    contract_address = web3.toChecksumAddress(contract_address)

    vow_like = web3.vns.contract(address=contract_address, abi=json_abi)
    return vow_like
    
