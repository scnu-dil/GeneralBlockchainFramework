
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from API.static import tianwen


parser = reqparse.RequestParser()

class BlockchainQuery(Resource):

    def __init__(self):
        pass

    def get_args(self, args, key):
        temp = args.get(key)
        return temp

    def getTransactionByHash(self):
        args = parser.parse_args()
        tsHash = self.get_args(args, 'tsHash')
        TransactionInfo = tianwen.getTransactionByHash(tsHash)

        res = {"transactionInfo": TransactionInfo}

        return res, 200








