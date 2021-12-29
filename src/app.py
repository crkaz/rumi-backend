from flask import Flask
from endpoints.todo_blueprint import todo_blueprint

app = Flask(__name__)

app.register_blueprint(todo_blueprint, url_prefix='/todo')


@app.route('/')
def index():
    return "OK"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
