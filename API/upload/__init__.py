


import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from error_code import *
from contracts.moduels import Tianwen

parser = reqparse.RequestParser()
parser.add_argument('item_N_line', type=str)
parser.add_argument('item_O_XH', type=str)
parser.add_argument('item_O_XFe', type=str)
parser.add_argument('item_O_loge', type=str)
parser.add_argument('item_C_XH', type=str)
parser.add_argument('item_C_XFe', type=str)
parser.add_argument('item_C_loge', type=str)

ITEMS  = {
    'AABCC01010':{ 'item_N_line' :'101' ,'item_O_XH':'102','item_O_XFe' :'103','item_O_loge' :'104','item_C_XH' :'105','item_C_XFe':'106','item_C_loge':'107'}
}

# contractFactory = ContractFactory()

class Upload(Resource):

    def __init__(self):
        pass

    # Postman
    def abort_if_item_exist(self, item_Element):
        if item_Element not in ITEMS:
            abort(404, message="Item{} doesn't exist".format(item_Element))

    def get_args(self, args, id, key):
        temp = args.get(key)
        if temp == '':
            temp = ITEMS[id][key]
        return temp

    # if TEMS[item_Element] is null return 404 error msg and 404
    def get(self, item_Element):
        self.abort_if_item_exist(item_Element)
        return ITEMS[item_Element]

    def put(self, item_Element):
        self.abort_if_item_exist(item_Element)
        args = parser.parse_args()

        item_N_line = self.get_args(args,item_Element,'item_N_line')
        item_O_XH = self.get_args(args,item_Element,'item_O_XH')
        item_O_XFe = self.get_args(args,item_Element,'item_O_XFe')
        item_O_loge = self.get_args(args,item_Element,'item_O_loge')
        item_C_XH = self.get_args(args,item_Element,'item_C_XH')
        item_C_XFe = self.get_args(args,item_Element,'item_C_XFe')
        item_C_loge = self.get_args(args,item_Element,'item_C_loge')


        new_item_Element = {'item_N_line' :item_N_line ,'item_O_XH':item_O_XH,'item_O_XFe' :item_O_XFe,' item_O_loge' :item_O_loge,'item_C_XH' :item_C_XH,'item_C_XFe':item_C_XFe,'item_C_loge':item_C_loge}
        ITEMS[item_Element] = new_item_Element

        # tianwen = Tianwen()
        # txHash = tianwen.set(item_Element, new_item_Element['item_N_line'], new_item_Element['item_O_XH'], new_item_Element['item_O_XFe'],
        #                      new_item_Element['item_O_loge'], new_item_Element['item_C_XH'], new_item_Element['item_C_XFe'], new_item_Element['item_C_loge'])

        txHash = "txHash"
        ITEMS["txHash"] = txHash

        return ITEMS, 200



