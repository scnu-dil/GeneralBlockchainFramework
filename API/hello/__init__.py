import flask_restful as restful

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world test , Im here'}





