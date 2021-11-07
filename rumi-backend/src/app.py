from datetime import datetime

from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rumi.db'
# db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html", date=datetime.now())
