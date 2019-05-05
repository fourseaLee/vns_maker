import json
#import vns_web3
from vns_web3 import Web3, HTTPProvider
import rlp
from web3.contract import ConciseContract
import vns_params
logger = vns_params.initLogger("dai.log")

web3 = Web3(HTTPProvider('http://192.168.0.40:8585'))

def getCat():
    json_file = open('dss/output/Cat.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Cat.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()
    
    cat = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return cat
    
def getDai():
    json_file = open('dss/output/Dai.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Dai.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    dai = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return dai
    

def getDaiJoin():
    json_file = open('dss/output/DaiJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/DainJoin.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    dai_join = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return dai_join
    
def getDSNote():
    json_file = open('dss/output/DSNote.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/DSNote.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    dsnote = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return dsnote
    
def getDSTokenLike():
    json_file = open('dss/output/DSTokenLike.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/DSTokenLike.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    dstoken_like = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return dstoken_like
    
def getETHJoin():
    json_file = open('dss/output/ETHJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/ETHJoin.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    eth_join = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return eth_join
    

def getFlapper():
    json_file = open('dss/output/Flapper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Flapper.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    flapper = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return flapper
    
def getFlippy():
    json_file = open('dss/output/Flippy.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Flippy.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    flippy = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return flippy
    

def getFlipper():
    json_file = open('dss/output/Flipper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Flipper.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    flipper = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return flipper
    
def getFlopper():
    json_file = open('dss/output/Flopper.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Flopper.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    flopper = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return flopper
    

def getFusspot():
    json_file = open('dss/output/Fusspot.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Fusspot.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    fusspot = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return fusspot
    
def getGemJoin():
    json_file = open('dss/output/GemJoin.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/GemJoin.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    gem_join = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return gem_join
    
def getHopeful():
    json_file = open('dss/output/Hopeful.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Hopeful.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    hopeful = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return hopeful
    
def getJug():
    json_file = open('dss/output/Jug.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    print(json_abi)

    bin_file = open('dss/output/Jug.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    jug = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return jug
    

def getVat():
    json_file = open('dss/output/Vat.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Vat.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()
    logger.info(json_abi)

    vat = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return vat
    
def getVow():
    json_file = open('dss/output/Vow.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/Vow.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    vow = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return vow
    

def getVowLike():
    json_file = open('dss/output/VowLike.abi', 'r')
    json_abi = json.load(json_file)
    json_file.close()
    
    bin_file = open('dss/output/VowLike.bin', 'r')
    contract_bin = bin_file.read()
    bin_file.close()

    vow_like = web3.vns.contract(abi=json_abi, bytecode=contract_bin)
    return vow_like
    
