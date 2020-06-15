


import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from contracts.client.bcosclient import BcosClient
import sys

parser = reqparse.RequestParser()
parser.add_argument('tsHash', type=str)

class Blockchain(Resource):
    def __init__(self):
        self.client = BcosClient()

    def get_args(self, args, key):
        temp = args.get(key)
        return temp

    def get(self, method):
        Msg = "method not found"
        status = 404
        args = parser.parse_args()

        if method == "getTransactionByHash":
            tsHash = self.get_args(args, 'tsHash')
            print ("hash:", tsHash)
            sys.stdout.flush()
            Msg, status = self.getTransactionByHash(tsHash)

        return Msg, status

    def getTransactionByHash(self, tsHash):
        TransactionInfo = self.client.getTransactionByHash(tsHash)
        return TransactionInfo, 200














# def getTransactionByHash(self, hash):
#     cmd = "getTransactionByHash"
#     common.check_hash(hash)
#     params = [self.groupid, hash]
#     return self.common_request(cmd, params)


# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getblocknumber
# def getBlockNumber(self):
#     cmd = "getBlockNumber"
#     params = [self.groupid]
#     num_hex = self.common_request(cmd, params)
#     return int(num_hex, 16)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getpbftview
# def getPbftView(self):
#     cmd = "getPbftView"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getsealerlist
#
# def getSealerList(self):
#     cmd = "getSealerList"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getobserverlist
#
# def getObserverList(self):
#     cmd = "getObserverList"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getconsensusstatus
# def getConsensusStatus(self):
#     cmd = "getConsensusStatus"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getsyncstatus
# def getSyncStatus(self):
#     cmd = "getSyncStatus"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getpeers
# def getPeers(self):
#     cmd = "getPeers"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getgrouppeers
# def getGroupPeers(self):
#     cmd = "getGroupPeers"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getnodeidlist
# def getNodeIDList(self):
#     cmd = "getNodeIDList"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getgrouplist
# def getGroupList(self):
#     cmd = "getGroupList"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getblockbyhash
# def getBlockByHash(self, block_hash, _includeTransactions=True):
#     cmd = "getBlockByHash"
#     common.check_hash(block_hash)
#     includeTransactions = common.check_and_trans_to_bool(_includeTransactions)
#     params = [self.groupid, block_hash, includeTransactions]
#     return self.common_request(cmd, params)
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getblockbynumber
#
# def getBlockByNumber(self, num, _includeTransactions=True):
#     """
#     get block according to number
#     """
#     cmd = "getBlockByNumber"
#     number = common.check_int_range(num)
#     includeTransactions = common.check_and_trans_to_bool(_includeTransactions)
#     params = [self.groupid, hex(number), includeTransactions]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getblockhashbynumber
# def getBlockHashByNumber(self, num):
#     cmd = "getBlockHashByNumber"
#     common.check_int_range(num)
#     params = [self.groupid, hex(num)]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_cn/release-2.0/docs/api.html#gettransactionbyhash
# def getTransactionByHash(self, hash):
#     cmd = "getTransactionByHash"
#     common.check_hash(hash)
#     params = [self.groupid, hash]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#gettransactionbyblockhashandindex
# def getTransactionByBlockHashAndIndex(self, hash, index):
#     cmd = "getTransactionByBlockHashAndIndex"
#     common.check_hash(hash)
#     common.check_int_range(index)
#     params = [self.groupid, hash, hex(index)]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#gettransactionbyblocknumberandindex
# def getTransactionByBlockNumberAndIndex(self, num, index):
#     cmd = "getTransactionByBlockNumberAndIndex"
#     common.check_int_range(num)
#     common.check_int_range(index)
#     params = [self.groupid, hex(num), hex(index)]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#gettransactionreceipt
# def getTransactionReceipt(self, hash):
#     cmd = "getTransactionReceipt"
#     common.check_hash(hash)
#     params = [self.groupid, hash]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getpendingtransactions
# def getPendingTransactions(self):
#     cmd = "getPendingTransactions"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getpendingtxsize
# def getPendingTxSize(self):
#     cmd = "getPendingTxSize"
#     params = [self.groupid]
#     tx_size = self.common_request(cmd, params)
#     return int(tx_size, 16)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#getcode
# def getCode(self, address):
#     cmd = "getCode"
#     fmt_addr = common.check_and_format_address(address)
#     params = [self.groupid, fmt_addr]
#     return self.common_request(cmd, params)
#
# # https://fisco-bcos-documentation.readthedocs.io/zh_CN/release-2.0/docs/api.html#gettotaltransactioncount
# def getTotalTransactionCount(self):
#     cmd = "getTotalTransactionCount"
#     params = [self.groupid]
#     return self.common_request(cmd, params)
#
#
