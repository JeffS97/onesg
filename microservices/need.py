from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/awsNeed'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/awsNeed'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Need(db.Model):
    __tablename__ = 'awsNeed'
    beneficiary_id = db.Column(db.Integer, primary_key=True)
    need_name = db.Column(db.String(255), primary_key=True)

    def __init__(self, beneficiary_id, need_name):
        self.beneficiary_id = beneficiary_id
        self.need_name = need_name

    def json(self):
        return {"beneficiary_id": self.beneficiary_id, "need_name": self.need_name}


# get all beneficaries in a list
@app.route("/allNeeds")
def get_all_beneficiary ():
    needs_list = Need.query.all()
    if len(needs_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "needs": [Need.json() for Need in needs_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Needs recorded."
        }
    ), 404


# create a need
@app.route("/need/add/<int:beneficiary_id>", methods=['POST'])
def add_beneficiary(beneficiary_id):
    data = request.get_json()
    need_name = data["need_name"]
    if (Need.query.filter(beneficiary_id==beneficiary_id).filter(need_name==need_name).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "beneficiary_id": beneficiary_id,
                    "need_name": need_name
                },
                "message": "Need already exists."
            }
        ), 400

    need = Need(beneficiary_id, need_name)
    
    try:
        db.session.add(need)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "beneficiary_id": beneficiary_id,
                    "need_name": need_name
                },
                "message": "An error occurred whilst adding the need."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": need.json()
        }
    ), 201


# pull all needs of a beneficiary
@app.route("/beneficiary/findById/<int:beneficiary_id>", methods=['POST'])
def find_by_beneficiary_id(beneficiary_id):
    needs_list = Need.query.filter(beneficiary_id==beneficiary_id).all()
    if len(needs_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "need": [Need.json() for Need in needs_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Needs recorded."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)