


import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from error_code import *

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
# item_Element string (key)
# item_N_line string
# item_O_XH string
# item_O_XFe string
# item_O_loge string
# item_C_XH string
# item_C_XFe string
# item_C_loge string

# get: http://127.0.0.1:5000/upload/AABCC01010
# put:  http://127.0.0.1:5000/upload/AABCC01010
#
#   item_N_line = 101
#   item_O_XH = 102
#   item_O_XFe = 103
#   item_O_loge = 104
#   item_C_XH = 105
#   item_C_XFe = 106
#   item_C_loge = 107

# Postman
def abort_if_item_exist(item_Element):
    if item_Element not in ITEMS:
        abort(404, message="Item{} doesn't exist".format(item_Element))

#避免局部修改造成数据值缺失
def get_args(args,id,key):
    temp = args.get(key)
    if temp == '':
        temp = ITEMS[id][key]
    return temp

class Upload(Resource):

    # if TEMS[item_Element] is null return 404 error msg and 404
    def get(self, item_Element):
        abort_if_item_exist(item_Element)
        return ITEMS[item_Element]

    def put(self, item_Element):
        abort_if_item_exist(item_Element)
        args = parser.parse_args()

        item_N_line = get_args(args,item_Element,'item_N_line')
        item_O_XH = get_args(args,item_Element,'item_O_XH')
        item_O_XFe = get_args(args,item_Element,'item_O_XFe')
        item_O_loge = get_args(args,item_Element,'item_O_loge')
        item_C_XH = get_args(args,item_Element,'item_C_XH')
        item_C_XFe = get_args(args,item_Element,'item_C_XFe')
        item_C_loge = get_args(args,item_Element,'item_C_loge')

        new_item_Element = {'item_N_line' :item_N_line ,'item_O_XH':item_O_XH,'item_O_XFe' :item_O_XFe,' item_O_loge' :item_O_loge,'item_C_XH' :item_C_XH,'item_C_XFe':item_C_XFe,'item_C_loge':item_C_loge}

        ITEMS[item_Element] = new_item_Element

        return new_item_Element,201

