
# coding=utf-8


from thirdParty.sdk.client.bcosclient import BcosClient
import os
from thirdParty.sdk.client.stattool import StatTool
from thirdParty.sdk.client.datatype_parser import DatatypeParser
from thirdParty.sdk.client.common.compiler import Compiler
from thirdParty.sdk.client_config import client_config
from thirdParty.sdk.client.bcoserror import BcosException, BcosError

# 实例化client
client = BcosClient()

# 调用查节点版本接口
res = client.getNodeVersion()
print("getClientVersion",res)

# 调用查节点块高接口
try:
    res = client.getBlockNumber()
    print("getBlockNumber",res)



except BcosError as e:
    print("bcos client error,",e.info())







































