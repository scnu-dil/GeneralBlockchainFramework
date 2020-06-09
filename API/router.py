
import os
import sys

sys.path.append("/root/GeneralBlockchainFramework")
sys.path.append("/root/GeneralBlockchainFramework/contracts")

from flask import Flask
import flask_restful as restful

from API.upload import *
from API.static import *
from API.blockchain import *

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(Upload, '/upload/<item_Element>')
api.add_resource(Blockchain, '/<method>')

#  malformed url rule:

if __name__ == '__main__':
    app.run(debug=True)

