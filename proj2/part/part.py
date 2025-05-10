from flask_restx import Namespace, Resource, fields

api = Namespace('part', description='Some information')

info_model = api.model('Info', {
    'id':   fields.String(required=True, description='Identifier'),
    'name': fields.String(required=True, description='Name')
})

SAMPLE = [{'id': '1111', 'name': 'Alex'}]

@api.route('/')
class InfoList(Resource):
    @api.marshal_list_with(info_model)
    def get(self):
        return SAMPLE

@api.route('/<id>')
@api.param('id', 'Identifier')
@api.response(404, 'Not found')
class InfoItem(Resource):
    @api.marshal_with(info_model)
    def get(self, id):
        for item in SAMPLE:
            if item['id'] == id:
                return item
        api.abort(404)
