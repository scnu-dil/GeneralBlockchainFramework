
import json
import traceback
from contracts import ContractManager

path = 'contracts/contracts/'

class Traffic(object):
    def __init__(self, contract_name = 'traffic', sol_file=path+'traffic.sol', abi_file=path+'traffic.abi', bin_file=path+'traffic.bin'):

        self.contractManager = ContractManager(sol_file, abi_file, bin_file, DEBUG=True)
        result, self.contractAddress = self.contractManager.checkContractExit(contract_name)
        if result is False:
            self.contract_abi, self.contract_info = self.contractManager.deploy()
            self.contractAddress = self.contract_info["contractAddress"]
        else:
            self.contract_abi, self.contractAddress = self.contractManager.getContractInfo(self.contractAddress)

    def constructJsonRecord(self, UUID, Url, FileMd5, Size, StorageIP, RemoteFileId, GroupName):
        Temp = {
            "UUID": UUID,
            "Url": Url,
            "FileMd5": FileMd5,
            "Size": Size,
            "StorageIP": StorageIP,
            "RemoteFileId": RemoteFileId,
            "GroupName": GroupName
        }
        return json.dumps(Temp)

    def set(self, UUID, Url, FileMd5, Size, StorageIP, RemoteFileId, GroupName):
        JsonRecord = self.constructJsonRecord(UUID, Url, FileMd5, Size, StorageIP, RemoteFileId, GroupName)
        args = [UUID, JsonRecord]
        try:
            txhash = self.contractManager.transaction(self.contract_abi, self.contractAddress, args)
            return txhash
        except:
            traceback.print_exc()
            return None

    def get(self, UUID):
        args = [UUID]
        try:
            response = self.contractManager.call(self.contractAddress, self.contract_abi, "get", args)
            return response
        except:
            traceback.print_exc()
            return None