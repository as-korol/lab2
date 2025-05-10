from flask_restx import Namespace, Resource

api = Namespace('templ', description='Template endpoint')

@api.route('/')
class Template(Resource):
    def get(self):
        return {'message': 'Это шаблонный ответ'}
