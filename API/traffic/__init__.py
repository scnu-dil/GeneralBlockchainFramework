
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from API.static import traffic

parser = reqparse.RequestParser()
parser.add_argument('UUID', type=str)
parser.add_argument('Url', type=str)
parser.add_argument('FileMd5', type=str)
parser.add_argument('Size', type=str)
parser.add_argument('StorageIP', type=str)
parser.add_argument('RemoteFileId', type=str)
parser.add_argument('GroupName', type=str)


class Traffic(Resource):
    def __init__(self):
        pass

    def get_args(self, args, key):
        temp = args.get(key)
        return temp

    def get(self):
        # UUID
        # transaction

        return {}

    def put(self, UUID):
        # self.abort_if_item_exist(item_Element)
        args = parser.parse_args()

        Url = self.get_args(args, 'Url')
        FileMd5 = self.get_args(args, 'FileMd5')
        Size = self.get_args(args,'Size')
        StorageIP = self.get_args(args, 'StorageIP')
        RemoteFileId = self.get_args(args, 'RemoteFileId')
        GroupName = self.get_args(args, 'GroupName')


        new_item_Element = {
            "UUID": UUID,
            "Url": Url,
            "FileMd5": FileMd5,
            "Size": Size,
            "StorageIP": StorageIP,
            "RemoteFileId": RemoteFileId,
            "GroupName": GroupName
        }

        # tianwen = Tianwen(
        tsHash = traffic.set(new_item_Element['UUID'], new_item_Element['Url'], new_item_Element['FileMd5'], new_item_Element["Size"], new_item_Element['StorageIP'], new_item_Element['RemoteFileId'], new_item_Element['GroupName'])

        # tsHash = "txHash"
        new_item_Element["tsHash"] = tsHash

        return new_item_Element, 200