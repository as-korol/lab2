from flask import Flask
from flask_restx import Api
from productapi.resources import api as product_ns

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['RESTX_JSON'] = {'ensure_ascii': False}

api = Api(
    app,
    version='1.0',
    title='API Продажи продуктов',
    description='CRUD, сортировка, статистика'
)
api.add_namespace(product_ns, path='/products')

if __name__ == "__main__":
    app.run(debug=True)
