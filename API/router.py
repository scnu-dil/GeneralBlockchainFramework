

from flask import Flask
import flask_restful as restful

from upload import *
from hello import *

app = Flask(__name__)
api = restful.Api(app)


api.add_resource(HelloWorld, '/helloWorld')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')





if __name__ == '__main__':
    app.run(debug=True)

