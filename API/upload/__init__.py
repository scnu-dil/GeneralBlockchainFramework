


import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)



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


class Upload(Resource):
    def get(self, item_Element):
        pass

    def put(self, item_Element):
        args = parser.parse_args()
        item_N_line = args['item_N_line']



