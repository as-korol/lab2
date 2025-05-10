from flask import Flask, jsonify, Blueprint
from flasgger import Swagger
from sitepart.sitepart import sitepart

app = Flask(__name__)
swagger = Swagger(app)

main = Blueprint("main", __name__,
                 template_folder='templates',
                 static_folder='static')

@main.route('/info/<about>/')
def info(about):
    """Example endpoint returning about info
    ---
    parameters:
      - name: about
        in: path
        type: string
        enum: ['all','version','author','year']
        required: true
        default: all
    definitions:
      About:
        type: string
    responses:
      200:
        description: A string
        schema:
          $ref: '#/definitions/About'
    """
    all_info = {
        'all': 'main_author 1.0 2020',
        'version': '1.0',
        'author': 'main_author',
        'year': '2020'
    }
    return jsonify({about: all_info.get(about, '')})

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(sitepart, url_prefix='/sitepart')

if __name__ == '__main__':
    app.run(debug=True)
