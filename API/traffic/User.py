
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from API.static import traffic

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('sex', type=str)
parser.add_argument('nativePlace', type=str)
parser.add_argument('address', type=str)
parser.add_argument('identityCard', type=str)
parser.add_argument('phone', type=str)
parser.add_argument('education', type=str)

class User(Resource):
    def __init__(self):
        pass

    def get_args(self, args, id, key):
        temp = args.get(key)
        return temp

    def get(self):
        response =   {
            "error_code": 0,
            "data": {
              "username": "李朝杰",
              "sex ": "男",
              "nativePlace ": "江西" ,
              "address": "深圳市南山区西丽新高路4号4010",
              "identityCard": "511XXXXXXXXXXXXXXX",
              "phone": "156XXXXXXXX",
              "education": "专科"
            }
          }
        return response, 200

    def post(self):
        args = parser.parse_args()

        uuid = self.get_args(args, 'uuid')
        username = self.get_args(args, 'username')
        sex = self.get_args(args, 'sex')
        nativePlace = self.get_args(args, 'nativePlace')
        address = self.get_args(args, 'address')
        identityCard = self.get_args(args, 'identityCard')
        phone = self.get_args(args, 'phone')
        education = self.get_args(args, 'education')

        response =   {
            "error_code": 0,
            "data": {
              "uuid": "4621d373cade4e83",
              "tsHash": "098f6bcd4621d373cade4e832627b4f6"
            }
          }
        return response, 200

    def put(self):
        args = parser.parse_args()

        username = self.get_args(args,'username')
        sex = self.get_args(args,'sex')
        nativePlace = self.get_args(args,'nativePlace')
        address = self.get_args(args,'address')
        identityCard = self.get_args(args,'identityCard')
        phone = self.get_args(args,'phone')
        education = self.get_args(args,'education')

        response =   {
            "error_code": 0,
            "data": {
              "uuid": "4621d373cade4e83",
              "tsHash": "098f6bcd4621d373cade4e832627b4f6"
            }
          }
        return response, 200












