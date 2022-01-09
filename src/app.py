from flask import Flask, render_template

from cache import cache
from config import config
from controllers.list_blueprint import list_blueprint
from controllers.list_item_blueprint import list_item_blueprint

app = Flask(__name__)
app.config.from_mapping(config)
cache.init_app(app)
app.register_blueprint(list_blueprint, url_prefix='/list')
app.register_blueprint(list_item_blueprint, url_prefix='/list/item')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
