
import flask_restful as restful,werkzeug
from flask_restful import reqparse, abort, Api, Resource
from API.static import tianwen

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
        audioFile.save("your_file_name.jpg")




