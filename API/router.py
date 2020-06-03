
import sys

path = "/root/GeneralBlockchainFramework"
sys.path.append(path)

from flask import Flask
import flask_restful as restful

from upload import *
from hello import *
from todo import *

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(HelloWorld, '/helloWorld')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(Upload, '/upload/<item_Element>')




if __name__ == '__main__':
    app.run(debug=True)

