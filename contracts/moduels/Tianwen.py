
from contracts import ContractManager
import json

class Tianwen(object):
    def __init__(self):
        pass

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
        return json.dump(record)

    def set(self, item_Element, item_N_line, item_O_XH, item_O_XFe, item_O_loge, item_C_XH, item_C_XFe, item_C_loge):
        JsonRecord = self.constructJsonRecord(item_Element, item_N_line, item_O_XH, item_O_XFe, item_O_loge, item_C_XH, item_C_XFe, item_C_loge)


    def get(self, item_Element):
        pass


































