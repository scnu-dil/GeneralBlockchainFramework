
import sys
sys.path.append("/Users/csx/GitProject/scnu-blcokchain")

from flask import Flask
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from util import sendFile

parser = reqparse.RequestParser()
parser.add_argument('item_N_line', type=str)
parser.add_argument('item_O_XH', type=str)
parser.add_argument('item_O_XFe', type=str)
parser.add_argument('item_O_loge', type=str)
parser.add_argument('item_C_XH', type=str)
parser.add_argument('item_C_XFe', type=str)
parser.add_argument('item_C_loge', type=str)
import werkzeug

class file_uplaod(Resource):
      def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parse.parse_args()
        audioFile = args['file']
        # audioFile.save("your_file_name.jpg")
        filecontent = audioFile.read()
        response = sendFile(filecontent)
        print (response.json())
          

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(file_uplaod, '/')

#  malformed url rule:

if __name__ == '__main__':
    app.run(debug=True)
















