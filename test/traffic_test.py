
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


# 实例化client
client = BcosClient()


sol_file  = "contracts/traffic.sol"
abi_file  = "contracts/traffic.abi"
bin_file  = "contracts/traffic.bin"

# 从文件加载abi定义
# sol_file = "contracts/traffic/traffic.sol"
# abi_file = "contracts/traffic.abi"

Compiler.compile_file(sol_file)
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi


# 部署合约
print("\n>>Deploy:---------------------------------------------------------------------")
with open(bin_file, 'r') as load_f:
    contract_bin = load_f.read()
    load_f.close()

result = client.deploy(contract_bin)
print("deploy",result)
print("new address : ",result["contractAddress"])
contract_name =  os.path.splitext(os.path.basename(abi_file))[0]
memo = "tx:"+result["transactionHash"]

#把部署结果存入文件备查
ContractNote.save_address(contract_name, result["contractAddress"], int(result["blockNumber"], 16), memo)







































