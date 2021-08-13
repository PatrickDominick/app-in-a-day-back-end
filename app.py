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
    high_score = db.Column(db.Integer, nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.high_score = high_score


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")


user_schema = UserSchema()


@app.route("/user/new", methods=["POST"])
def new_user():
    if request.content_type != "application/json":
        return jsonify("JSON PLZ")

    user_info = request.get_json()
    username = user_info.get("username")
    password = user_info.get("password")

    new_record = User(username, password)

    db.session.add(new_record)
    db.session.commit()

    return jsonify("New user added")



if __name__ == "__main__":
    app.run(debug=True)