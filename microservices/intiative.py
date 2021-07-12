from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/ESD5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Initiative(db.Model):
    __tablename__ = 'Initiatives'

    initiative_id = db.Column(db.Integer, primary_key=True)
    P_name = db.Column(db.String(150), nullable=False)
    Username = db.Column(db.String(150), nullable=False)
    Email = db.Column(db.String(200), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(200), nullable=False)
    Allergy = db.Column(db.String(200), nullable=True)
    ChatId = db.Column(db.String(200), nullable=True)
    Payment = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, initiative_id, Username, P_name, Email, Age, Address, Allergy, ChatId, Payment, password):
        self.initiative_id = initiative_id
        self.P_name = P_name
        self.Username = Username
        self.Email = Email
        self.Age = Age
        self.Address = Address
        self.Allergy = Allergy
        self.ChatId = ChatId
        self.Payment = Payment
        self.password = password

    def json(self):
        return {"initiative_id": self.initiative_id, "P_name": self.P_name, "Email": self.Email, "Age": self.Age, "Allergy": self.Allergy, "Address": self.Address, "ChatId": self.ChatId, "Payment": self.Payment, "password": self.password}


# get all initiatives in a list
@app.route("/initiatives")
def get_all_initiatives():
    initiative_list = Initiative.query.all()
    if len(initiative_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "initiatives": [initiative.json() for initiative in initiative_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no initiatives."
        }
    ), 404


# pull specific initiative's details
@app.route("/initiative/findByInitiativeId/<int:iid>", methods=['POST'])
def find_by_initiative_id(iid):
    # data = request.get_json()
    # iid = data['initiative_id']
    initiative = Initiative.query.filter_by(initiative_id=iid).first()
    if initiative:
        return jsonify(
            {
                "code": 200,
                "data": initiative.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Initiative not found."
        }
    ), 404


# add new initiative
@app.route("/initiative/add/<int:iid>", methods=['POST'])
def add_initiative(iid):
    if (Initiative.query.filter_by(initiative_id=iid).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "initiative_id": iid
                },
                "message": "Initiative already exists."
            }
        ), 400
 
    data = request.get_json()
    initiative = Initiative(iid, **data)
 
    try:
        db.session.add(initiative)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "initiative_id": iid
                },
                "message": "An error occurred whilst adding the initiative."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": initiative.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)