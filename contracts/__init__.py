# coding=utf-8

from thirdParty.sdk.client.bcosclient import BcosClient
import os
from thirdParty.sdk.client.stattool import StatTool
from thirdParty.sdk.client.datatype_parser import DatatypeParser
from thirdParty.sdk.client.common.compiler import Compiler
from thirdParty.sdk.client_config import client_config
from thirdParty.sdk.client.bcoserror import BcosException, BcosError
from eth_utils import to_checksum_address
from thirdParty.sdk.client.contractnote import ContractNote

class ContractManager(object):

    def __init__(self, sol_file, abi_file, bin_file, DEBUG=True):
        # 实例化client
        self.client = BcosClient()
        self.sol_file = sol_file
        self.abi_file = abi_file
        self.bin_file = bin_file
        self.DEBUG = DEBUG

        self.data_parser = DatatypeParser()
        self.data_parser.load_abi_file(self.abi_file)


    def compile(self):
        if os.path.isfile(client_config.solc_path) or os.path.isfile(client_config.solcjs_path):
            Compiler.compile_file(self.sol_file)

    def deploy(self):
        contract_abi = self.data_parser.contract_abi

        # 部署合约
        if self.DEBUG:
            print("\n>>Deploy:---------------------------------------------------------------------")

        with open(self.bin_file, 'r') as load_f:
            contract_bin = load_f.read()
            load_f.close()

        result = self.client.deploy(contract_bin)

        if self.DEBUG:
            print("deploy", result)
            print("new address : ", result["contractAddress"])

        contract_name = os.path.splitext(os.path.basename(self.abi_file))[0]
        memo = "tx:" + result["transactionHash"]

        # 把部署结果存入文件备查
        ContractNote.save_address(contract_name, result["contractAddress"], int(result["blockNumber"], 16), memo)
        return contract_abi, result

    # url = "http://47.113.185.200/group1/M00/00/00/rBjqU16nnLiASd4YAMVnXomRO6M785.mp4"
    # hashvalue = "c3c93aae6dbed266a0dc55a517960273bc0b79c5ca13afe9ca5ab2d3825540f4"
    # args = [url, hashvalue]

    def transaction(self, contract_abi, contract_info, args):
        to_address = contract_info['contractAddress']  # use new deploy address

        # 发送交易，调用一个改写数据的接口
        if self.DEBUG:
            print("\n>>sendRawTransaction:----------------------------------------------------------")
            print (to_address)

        receipt = self.client.sendRawTransactionGetReceipt(to_address, contract_abi, "set", args)
        txhash = receipt['transactionHash']

        if self.DEBUG:
        # 解析receipt里的log
            print("\n>>parse receipt and transaction:----------------------------------------------------------")
            print("transaction hash: ", txhash)
            logresult = self.data_parser.parse_event_logs(receipt["logs"])
            i = 0
            for log in logresult:
                if 'eventname' in log:
                    i = i + 1
                    print("{}): log name: {} , data: {}".format(i, log['eventname'], log['eventdata']))

            # 获取对应的交易数据，解析出调用方法名和参数
            txresponse = self.client.getTransactionByHash(txhash)
            inputresult = self.data_parser.parse_transaction_input(txresponse['input'])
            print("transaction input parse:", txhash)
            print(inputresult)

        return txhash

    def call(self, contract_address, contract_abi, method, args=None):

        # 调用一下call，获取数据
        try:
            res = self.client.call(contract_address, contract_abi, method, args)
            return True, args
        except:
            import traceback
            return False, "call contract error"











































