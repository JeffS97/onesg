from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/awsInitiative'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)

class Initiative(db.Model):
    __tablename__ = 'awsInitiative'

    initiative_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    initiative_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    volunteer_id = db.Column(db.Integer, nullable=False)
    charity_id = db.Column(db.Integer, nullable=True)
    support = db.Column(db.String(250), nullable=True)
    category = db.Column(db.String(250), nullable=True)
    volunteer_goal = db.Column(db.Integer, nullable=False)
    donation_goal = db.Column(db.Integer, nullable=False)
    beneficiary_type = db.Column(db.String(250), nullable=True)
    skills_required = db.Column(db.String(250), nullable=True)

    def __init__(self, volunteer_id, initiative_name, description, charity_id, support, category, volunteer_goal, donation_goal, beneficiary_type, skills_required):
        # self.initiative_id = initiative_id
        self.initiative_name = initiative_name
        self.description = description
        self.volunteer_id = volunteer_id
        self.charity_id = charity_id
        self.support = support
        self.category = category
        self.volunteer_goal = volunteer_goal
        self.donation_goal = donation_goal
        self.beneficiary_type = beneficiary_type
        self.skills_required = skills_required

    def json(self):
        return {"initiative_id": self.initiative_id, "initiative_name": self.initiative_name, "description": self.description, "volunteer_id": self.volunteer_id, "charity_id": self.charity_id, "support": self.support, "category": self.category, "volunteer_goal": self.volunteer_goal, "donation_goal": self.donation_goal, "skills_required": self.skills_required, "beneficiary_type": self.beneficiary_type}


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
@app.route("/initiative/add", methods=['POST'])
def add_initiative():
 
    data = request.get_json()
    print(data)
    initiative = Initiative(**data)
 
    try:
        db.session.add(initiative)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
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