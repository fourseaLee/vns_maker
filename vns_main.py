import time
from vns_web3 import Web3, HTTPProvider
import json
import vns_params
import vns_codeabi
import vns_dai

vns_params.configuer_file = 'configure.json'
params = vns_params.readParams()
logger = vns_params.initLogger("maker.log")

def main():
    logger.info("maker begin-----------------------------")
    vat_contract = vns_dai.getVat();
    logger.info(vat_contract)
    
if __name__ == '__main__':
    main()
