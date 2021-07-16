from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/awsBeneficiary'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/awsBeneficiary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Beneficiary(db.Model):
    __tablename__ = 'awsBeneficiary'
    beneficiary_id = db.Column(db.Integer, primary_key=True)
    beneficiary_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    sex = db.Column(db.String(250), nullable=True)
    description = db.Column(db.String(250), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    dateOfBirth = db.Column(db.Date, nullable=False)

    def __init__(self, beneficiary_id, username, beneficiary_name, email, address, password, sex, description, postal_code, dateOfBirth):
        self.beneficiary_id = beneficiary_id
        self.beneficiary_name = beneficiary_name
        self.username = username
        self.email = email
        self.address = address
        self.password = password
        self.sex = sex
        self.description = description
        self.postal_code = postal_code
        self.dateOfBirth = dateOfBirth

    def json(self):
        return {"beneficiary_id": self.beneficiary_id, "beneficiary_name": self.beneficiary_name, "email": self.email,"password": self.password, "username": self.username, "sex": self.sex, "description": self.description, "postal_code": self.postal_code, "dateOfBirth": self.dateOfBirth, "address":self.address}


# get all beneficaries in a list
@app.route("/beneficiary")
def get_all_beneficiary ():
    beneficiary_list = Beneficiary.query.all()
    if len(beneficiary_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "beneficiary": [Beneficiary.json() for Beneficiary in beneficiary_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no registered beneficiary."
        }
    ), 404


# create beneficiary account
@app.route("/beneficiary/add/<int:beneficiary_id>", methods=['POST'])
def add_beneficiary(beneficiary_id):
    if (Beneficiary.query.filter_by(beneficiary_id=beneficiary_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "beneficiary_id": beneficiary_id
                },
                "message": "Beneficiary already exists."
            }
        ), 400

    data = request.get_json()
    beneficiary = Beneficiary(beneficiary_id, **data)
    
    try:
        db.session.add(beneficiary)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "beneficiary_id": beneficiary_id
                },
                "message": "An error occurred whilst adding the volunteer."
            }
        ), 500
    return jsonify(
        {
            "code": 201,
            "data": beneficiary.json()
        }
    ), 201


# pull beneficiary's personal particulars
@app.route("/beneficiary/findById/<int:beneficiary_id>", methods=['POST'])
def find_by_beneficiary_id(beneficiary_id):
    beneficiary = Beneficiary.query.filter_by(beneficiary_id=beneficiary_id).first()
    if beneficiary:
        return jsonify(
            {
                "code": 200,
                "data": beneficiary.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Beneficiary not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)