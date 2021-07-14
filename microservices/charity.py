from operator import add, pos
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/awsCharity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Charity(db.Model):
    __tablename__ = 'awsCharity'

    charity_id = db.Column(db.Integer, primary_key=True)
    charity_name = db.Column(db.String(150), nullable=False)
    c_username = db.Column(db.String(150), nullable=False)
    c_email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    chat_id = db.Column(db.String(250), nullable=False)
    beneficiary_type = db.Column(db.String(250), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(250), nullable=False)

    def __init__(self, charity_id, c_username, charity_name, c_email, password, chat_id, beneficiary_type, postal_code, address):
        self.charity_id = charity_id
        self.charity_name = charity_name
        self.c_username = c_username
        self.c_email = c_email
        self.password = password
        self.chat_id = chat_id
        self.beneficiary_type = beneficiary_type
        self.postal_code = postal_code
        self.address = address

    def json(self):
        return {"charity_id": self.charity_id, "charity_name": self.charity_name, "c_email": self.c_email, "password": self.password, "c_username": self.c_username, "chat_id": self.chat_id, "address": self.address, "postal_code": self.postal_code, "beneficiary_type": self.beneficiary_type}


# get all charities in a list
@app.route("/charities")
def get_all_charities():
    charity_list = Charity.query.all()
    if len(charity_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "charities": [charity.json() for charity in charity_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no charities."
        }
    ), 404


# create charity account
@app.route("/charity/add/<int:cid>", methods=['POST'])
def add_charity(cid):
    if (Charity.query.filter_by(charity_id=cid).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "charity_id": cid
                },
                "message": "Charity already exists."
            }
        ), 400
 
    data = request.get_json()
    charity = Charity(cid, **data)
 
    try:
        db.session.add(charity)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "charity_id": cid
                },
                "message": "An error occurred whilst adding the charity."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": charity.json()
        }
    ), 201


# pull specific charity's information
@app.route("/charity/findByCid/<int: cid>", methods=['POST'])
def find_by_cid(cid):
    # data = request.get_json()
    # cid = data['charity_id']
    charity = Charity.query.filter_by(charity_id=cid).first()
    if charity:
        return jsonify(
            {
                "code": 200,
                "data": charity.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Charity not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)