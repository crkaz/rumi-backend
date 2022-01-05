from flask import Blueprint
from cache import cache

list_item_blueprint = Blueprint('list_item_blueprint', __name__)


def create_item():
    return 'create'


@list_item_blueprint.route('/read')
def read_items():
    return 'read'


@list_item_blueprint.route('/update')
def update_item():
    return 'update'


@list_item_blueprint.route('/delete')
def delete_item():
    return 'delete'
