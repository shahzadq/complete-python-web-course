from flask import Blueprint

item_blueprint = Blueprint('items', __name__)


@item_blueprint.route('/item/<string:name>')
def item_page(name):
    pass


@item_blueprint.route('/load')
def load_item():
    pass
