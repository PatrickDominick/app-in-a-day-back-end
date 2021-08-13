from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username")


user_schema = UserSchema()



class Tokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_name = db.Column(db.String, nullable=False, unique=True)
    base_value = db.Column(db.Integer)
    token_rule = db.Column(db.String)

    def __init__(token_name, base_value, token_rule):
        self.token_name = token_name
        self.base_value = base_value
        self.token_rule = token_rule





if __name__ == "__main__":
    app.run(debug=True)