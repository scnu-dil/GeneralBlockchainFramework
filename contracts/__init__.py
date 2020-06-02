# coding=utf-8
import os
import sys

Path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(Path)

from contracts.client.bcosclient import BcosClient
from contracts.client.stattool import StatTool
from contracts.client.datatype_parser import DatatypeParser
from contracts.client.common.compiler import Compiler
from contracts.client_config import client_config
from contracts.client.bcoserror import BcosException, BcosError
from contracts.eth_utils import to_checksum_address
from contracts.client.contractnote import ContractNote
from contracts.client.common.transaction_common import TransactionCommon
from client.bcoserror import CompilerNotFound, CompileError


class ContractManager(object):

    def __init__(self, sol_file, abi_file, bin_file, DEBUG=True):
        # 实例化client
        self.client = BcosClient()
        self.sol_file = sol_file
        self.abi_file = abi_file
        self.bin_file = bin_file
        self.DEBUG = DEBUG

        self.data_parser = DatatypeParser()

        if os.path.isfile(self.abi_file):
            self.compile()

        self.data_parser.load_abi_file(self.abi_file)


    def compile(self):
        if os.path.isfile(client_config.solc_path) or os.path.isfile(client_config.solcjs_path):
            try:
                Compiler.compile_file(self.sol_file, output_path="contracts/contracts")
            except CompileError:
                print (CompileError)
        else:
            print (client_config.solc_path)

    def checkContractExit(self, contract_name):
        address = ContractNote.get_contract_addresses(contract_name)
        if address is None:
            return False, None
        else:
            return True, address

    def getContractInfo(self, contractAddress):
        contract_info = self.client.getTransactionByHash(contractAddress)
        contract_abi = TransactionCommon.gen_contract_abi(self.abi_file)
        return contract_abi, contract_info


    def deploy(self):
        contract_abi = self.data_parser.contract_abi

        # 部署合约
        if self.DEBUG:
            print("\n>>Deploy:---------------------------------------------------------------------")

        with open(self.bin_file, 'r') as load_f:
            contract_bin = load_f.read()
            load_f.close()

        contract_info = self.client.deploy(contract_bin)

        if self.DEBUG:
            print("deploy", contract_info)
            print("new address : ", contract_info["contractAddress"])

        contract_name = os.path.splitext(os.path.basename(self.abi_file))[0]
        memo = "tx:" + contract_info["transactionHash"]

        # 把部署结果存入文件备查
        ContractNote.save_address(contract_name, contract_info["contractAddress"], int(contract_info["blockNumber"], 16), memo)
        ContractNote.save_contract_address(contract_name, contract_info["contractAddress"])

        return contract_abi, contract_info

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
            response = self.client.call(contract_address, contract_abi, method, args)
            return True, response
        except:
            import traceback
            return False, "call contract error"












































