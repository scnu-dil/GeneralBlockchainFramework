
import flask_restful as restful
from flask_restful import reqparse, abort, Api, Resource
from API.static import traffic

parser = reqparse.RequestParser()
parser.add_argument('uuid', type=str)
parser.add_argument('appearance', type=str)
parser.add_argument('morality	', type=str)
parser.add_argument('learn', type=str)
parser.add_argument('communication', type=str)
parser.add_argument('attendance', type=str)
parser.add_argument('responsibility', type=str)
parser.add_argument('initiatve', type=str)
parser.add_argument('teamwork', type=str)
parser.add_argument('potential', type=str)


class KPI(Resource):
    def __init__(self):
        pass

    def put(self):
        args = parser.parse_args()

        uuid = self.get_args(args,'uuid')
        appearance = self.get_args(args,'appearance')
        morality = self.get_args(args,'morality')
        learn = self.get_args(args,'learn')
        communication = self.get_args(args,'communication')
        attendance = self.get_args(args,'attendance')
        responsibility = self.get_args(args,'responsibility')
        initiatve = self.get_args(args,'initiatve')
        teamwork = self.get_args(args,'teamwork')
        potential = self.get_args(args,'potential')


        response =   {
            "error_code": 0,
            "data": {
              "uuid": "4621d373cade4e83",
              "tsHash": "098f6bcd4621d373cade4e832627b4f6"
            }
          }
        return response, 200
