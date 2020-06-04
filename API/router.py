
import os
import sys

sys.path.append("/root/GeneralBlockchainFramework")
sys.path.append("/root/GeneralBlockchainFramework/contracts")

from flask import Flask
import flask_restful as restful

from API.upload import *
from API.hello import *
from API.todo import *
from API.static import *

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(HelloWorld, '/helloWorld')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(Upload, '/upload/<item_Element>')




if __name__ == '__main__':
    app.run(debug=True)

