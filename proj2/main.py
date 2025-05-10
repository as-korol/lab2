from flask import Flask
from flask_restx import Api, Resource
from part.part import api as part_ns
from part.parttmpl import api as tmpl_ns

app = Flask(__name__)
api = Api(app,
          version='1.0',
          title='Demo API',
          description='Пример Flask-RESTX')

# Main Namespace
main_ns = api.namespace('main', description='Main APIs')

@main_ns.route('/')
class Main(Resource):
    def get(self):
        return {'status': 'Got new data'}
    def post(self):
        return {'status': 'Posted new data'}

# Регистрация всех Namespace
api.add_namespace(main_ns, path='/main')
api.add_namespace(part_ns, path='/part')
api.add_namespace(tmpl_ns, path='/templ')

if __name__ == "__main__":
    app.run(debug=True)
