#coding=UTF-8
import sys
sys.path.append('..')
from temp import ContractManager
import json
import traceback

path = '/root/GeneralBlockchainFramework/temp/content/'

class Tianwen(object):
    def __init__(self, contract_name = 'TianwenKV', sol_file=path+'TianwenKV.sol', abi_file=path+'TianwenKV.abi', bin_file=path+'TianwenKV.bin'):

        self.contractManager = ContractManager(sol_file, abi_file, bin_file, DEBUG=True)
        # checkContractExit这个函数出问题了
        result, self.contractAddress = self.contractManager.checkContractExit(contract_name)
        if result is False:
            self.contract_abi, self.contract_info = self.contractManager.deploy()
            self.contractAddress = self.contract_info["contractAddress"]
        else:
            self.contract_abi, self.contract_info = self.contractManager.getContractInfo(self.contractAddress)

    # try, catch
    def constructJsonRecord(self, item_Element, item_N_line, item_O_XH, item_O_XFe, item_O_loge, item_C_XH, item_C_XFe, item_C_loge):
        record = {
            "item_Element": item_Element,
            "item_N_line": item_N_line,
            "item_O_XH": item_O_XH,
            "item_O_XFe": item_O_XFe,
            "item_O_loge": item_O_loge,
            "item_C_XH": item_C_XH,
            "item_C_XFe": item_C_XFe,
            "item_C_loge": item_C_loge
        }
        return json.dumps(record)

    def set(self, item_Element, item_N_line, item_O_XH, item_O_XFe, item_O_loge, item_C_XH, item_C_XFe, item_C_loge):
        JsonRecord = self.constructJsonRecord(item_Element, item_N_line, item_O_XH, item_O_XFe, item_O_loge, item_C_XH, item_C_XFe, item_C_loge)
        args = [item_Element, JsonRecord]
        try:
            txhash = self.contractManager.transaction(self.contract_abi, self.contract_info, args)
            return txhash
        except:
            traceback.print_exc()
            return None

    def get(self, item_Element):
        args = [item_Element]
        try:
            response = self.contractManager.call(self.contractAddress, self.contract_abi, "get", args)
            return response
        except:
            traceback.print_exc()
            return None



































