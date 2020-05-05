
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

# 从文件加载abi定义
sol_file  ="contracts/SimpleInfo.sol"
abi_file  ="contracts/SimpleInfo.abi"

Compiler.compile_file(sol_file)
data_parser = DatatypeParser()
data_parser.load_abi_file(abi_file)
contract_abi = data_parser.contract_abi

# 部署合约
print("\n>>Deploy:---------------------------------------------------------------------")
with open("contracts/SimpleInfo.bin", 'r') as load_f:
    contract_bin = load_f.read()
    load_f.close()
result = client.deploy(contract_bin)
print("deploy",result)
print("new address : ",result["contractAddress"])
contract_name =  os.path.splitext(os.path.basename(abi_file))[0]
memo = "tx:"+result["transactionHash"]

#把部署结果存入文件备查
ContractNote.save_address(contract_name, result["contractAddress"], int(result["blockNumber"], 16), memo)

#发送交易，调用一个改写数据的接口
print("\n>>sendRawTransaction:----------------------------------------------------------")
to_address = result['contractAddress'] #use new deploy address
args = ['simplename', 2024, to_checksum_address('0x7029c502b4F824d19Bd7921E9cb74Ef92392FB1c')]

receipt = client.sendRawTransactionGetReceipt(to_address,contract_abi,"set",args)
print("receipt:",receipt)

#解析receipt里的log
print("\n>>parse receipt and transaction:----------------------------------------------------------")
txhash = receipt['transactionHash']
print("transaction hash: " ,txhash)
logresult = data_parser.parse_event_logs(receipt["logs"])
i = 0
for log in logresult:
    if 'eventname' in log:
        i = i + 1
        print("{}): log name: {} , data: {}".format(i,log['eventname'],log['eventdata']))
#获取对应的交易数据，解析出调用方法名和参数

txresponse = client.getTransactionByHash(txhash)
inputresult = data_parser.parse_transaction_input(txresponse['input'])
print("transaction input parse:",txhash)
print(inputresult)

#解析该交易在receipt里输出的output,即交易调用的方法的return值
outputresult  = data_parser.parse_receipt_output(inputresult['name'], receipt['output'])
print("receipt output :",outputresult)

#调用一下call，获取数据
print("\n>>Call:------------------------------------------------------------------------")
res = client.call(to_address,contract_abi,"getbalance")
print("call getbalance result:",res)
res = client.call(to_address,contract_abi,"getbalance1",[100])
print("call getbalance1 result:",res)
res = client.call(to_address,contract_abi,"getname")
print("call getname:",res)
res = client.call(to_address,contract_abi,"getall")
print("call getall result:",res)
print("demo_tx,total req {}".format(client.request_counter))
client.finish()