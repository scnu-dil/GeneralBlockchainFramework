
from contracts.moduels import Tianwen

class ContractFactory(object):

    def __init__(self):
        self.tianwen = Tianwen.Tianwen()

    def getTianwen(self):
        return self.tianwen