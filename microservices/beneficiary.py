from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)
CORS(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/awsBeneficiary'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/awsBeneficiary'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Beneficiary(db.Model):
    __tablename__ = 'awsBeneficiary'
    beneficiary_type = db.Column(db.String(100), nullable=False)
    beneficiary_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150),  primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    sex = db.Column(db.String(250), nullable=True)
    postal_code = db.Column(db.Integer, nullable=True)
    dateOfBirth = db.Column(db.Date, nullable=False)
    interest = db.Column(db.String(250), nullable=True)

    def __init__(self, username, beneficiary_name, email, sex, postal_code, dateOfBirth, beneficiary_type, interest):
        self.beneficiary_name = beneficiary_name
        self.beneficiary_type = beneficiary_type
        self.username = username
        self.email = email
        self.sex = sex
        self.postal_code = postal_code
        self.dateOfBirth = dateOfBirth
        self.interest = interest

    def json(self):
        return { "beneficiary_name": self.beneficiary_name, "beneficiary_type": self.beneficiary_type, "email": self.email, "username": self.username, "sex": self.sex,  "postal_code": self.postal_code, "dateOfBirth": self.dateOfBirth, "interest": self.interest}


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
@app.route("/beneficiary/add", methods=['POST'])
def add_beneficiary():

    data = request.get_json()
    beneficiary = Beneficiary(**data)
    
    try:
        db.session.add(beneficiary)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "error": "error"
                },
                "message": "An error occurred whilst adding the beneficiary."
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