from flask import Blueprint
from cache import cache
from static.constants import ONE_MIN

CACHE_KEY = 'all_lists'

list_blueprint = Blueprint('list_blueprint', __name__)

@list_blueprint.route('/create')
def create_list():
    return 'create'


@cache.cached(timeout=ONE_MIN, key_prefix=CACHE_KEY)
@list_blueprint.route('/read')
def read_lists():
    return 'read'


@list_blueprint.route('/update')
def update_list():
    return 'update'


@list_blueprint.route('/delete')
def delete_list():
    return 'delete'
