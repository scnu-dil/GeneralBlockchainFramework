
import os
import sys

sys.path.append("/root/GeneralBlockchainFramework")
sys.path.append("/root/GeneralBlockchainFramework/contracts")

from flask import Flask
import flask_restful as restful

from API.upload import *
from API.static import tianwen, traffic
from API.blockchain import *


from API.traffic.User import User
from API.traffic.Record import Record
from API.traffic.KPI import KPI

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(Upload, '/upload/<item_Element>')
api.add_resource(Blockchain, '/<method>')
api.add_resource(User, '/traffic/api/user')
api.add_resource(Record, '/traffic/api/record')
api.add_resource(KPI, '/traffic/api/kpi')



# git@github.com:scnu-dil/GeneralBlockchainFramework.git


#  malformed url rule:

if __name__ == '__main__':
    app.run(debug=True)

