from flask import Blueprint

todo_blueprint = Blueprint('todo_blueprint', __name__)


@todo_blueprint.route('/create')
def create_todo():
    return 'create'


@todo_blueprint.route('/read')
def read_todo():
    return 'read'


@todo_blueprint.route('/update')
def update_todo():
    return 'update'


@todo_blueprint.route('/delete')
def delete_todo():
    return 'delete'
