from flask_restx import Namespace, Resource, fields, reqparse

api = Namespace('products', description='Управление продуктами')

product_model = api.model('Product', {
    'id':           fields.Integer(readonly=True),
    'name':         fields.String(required=True),
    'manufacturer': fields.String(required=True),
    'weight':       fields.Float(required=True),
    'price':        fields.Float(required=True),
    'category':     fields.String(required=True)
})

PRODUCTS = []
_counter = 0

# Парсеры
sort_parser = reqparse.RequestParser()
sort_parser.add_argument('sort_by', choices=('name','manufacturer','weight','price','category'))
sort_parser.add_argument('order',   choices=('asc','desc'), default='asc')

stats_parser = reqparse.RequestParser()
stats_parser.add_argument('field', choices=('weight','price'), required=True)

@api.route('/')
class ProductList(Resource):
    @api.expect(sort_parser)
    @api.marshal_list_with(product_model)
    def get(self):
        args = sort_parser.parse_args()
        data = PRODUCTS.copy()
        if args['sort_by']:
            data.sort(key=lambda x: x[args['sort_by']], reverse=(args['order']=='desc'))
        return data

    @api.expect(product_model, validate=True)
    @api.marshal_with(product_model, code=201)
    def post(self):
        global _counter
        _counter += 1
        item = api.payload
        item['id'] = _counter
        PRODUCTS.append(item)
        return item, 201

@api.route('/<int:id>')
@api.param('id', 'ID продукта')
@api.response(404, 'Не найдено')
class Product(Resource):
    @api.marshal_with(product_model)
    def get(self, id):
        for p in PRODUCTS:
            if p['id'] == id:
                return p
        api.abort(404)

    def delete(self, id):
        for p in PRODUCTS:
            if p['id'] == id:
                PRODUCTS.remove(p)
                return '', 204
        api.abort(404)

    @api.expect(product_model, validate=True)
    @api.marshal_with(product_model)
    def put(self, id):
        for p in PRODUCTS:
            if p['id'] == id:
                for k, v in api.payload.items():
                    if k != 'id': p[k] = v
                return p
        api.abort(404)

@api.route('/stats')
class Stats(Resource):
    @api.expect(stats_parser)
    def get(self):
        args = stats_parser.parse_args()
        field = args['field']
        if not PRODUCTS:
            api.abort(404, 'Нет данных')
        vals = [p[field] for p in PRODUCTS]
        return {'min': min(vals), 'max': max(vals), 'avg': sum(vals)/len(vals)}
