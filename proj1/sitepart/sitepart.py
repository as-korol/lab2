from flask import Blueprint, jsonify

sitepart = Blueprint("sitepart", __name__,
                     template_folder='templates',
                     static_folder='static')

@sitepart.route('/colors/<palette>/')
def colors(palette):
    """Example endpoint returning a list of colors by palette
    ---
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['all','rgb','cmyk']
        required: true
        default: all
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              type: string
    responses:
      200:
        description: A list of colors
    """
    palettes = {
        'cmyk': ['cian', 'magenta', 'yellow', 'black'],
        'rgb': ['red', 'green', 'blue']
    }
    if palette == 'all':
        return jsonify(palettes)
    return jsonify({palette: palettes.get(palette, [])})
