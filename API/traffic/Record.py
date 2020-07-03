
from flask import Flask
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from util import sendFile
import werkzeug


parse = reqparse.RequestParser()
parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
parse.add_argument('name', type=str)
parse.add_argument('plates', type=str)
parse.add_argument('phone', type=str)
parse.add_argument('time', type=str)
parse.add_argument('address', type=str)
parse.add_argument('speed', type=str)
parse.add_argument('direction', type=str)

class Record(Resource):
    def post(self):
        args = parse.parse_args()
        audioFile = args['file']
        name = args['name']
        plates = args['plates']
        phone = args['phone']
        time = args['time']
        address = args['address']
        speed = args['speed']
        direction = args['direction']

        filecontent = audioFile.read()
        data = sendFile(filecontent)
        response = {
            "error_code": 0,
            "data": data
        }
        return response, 200


app = Flask(__name__)
api = restful.Api(app)

api.add_resource(file_uplaod, '/')

#  malformed url rule:

if __name__ == '__main__':
    app.run(debug=True)

