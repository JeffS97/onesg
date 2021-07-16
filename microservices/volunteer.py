from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import json
import requests
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/awsVolunteer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Volunteer(db.Model):
    __tablename__ = 'awsVolunteer'

    volunteer_id = db.Column(db.Integer, primary_key=True)
    volunteer_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    # chat_id = db.Column(db.String(200), nullable=True)
    payment = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(250), nullable=False)
    skills = db.Column(db.String(250), nullable=False)
    credentials = db.Column(db.String(250), nullable=False)
    sex = db.Column(db.String(250), nullable=True)
    description = db.Column(db.String(250), nullable=True)
    areas_of_interest = db.Column(db.String(250), nullable=False)
    postal_code = db.Column(db.Integer, nullable=True)

    def __init__(self, volunteer_id, username, volunteer_name, email, age, address, payment, password, skills, credentials, sex, description, areas_of_interest, postal_code):
        self.volunteer_id = volunteer_id
        self.volunteer_name = volunteer_name
        self.username = username
        self.email = email
        self.age = age
        self.address = address
        # self.chat_id = chat_id
        self.payment = payment
        self.password = password
        self.skills = skills
        self.credentials = credentials
        self.sex = sex
        self.description = description
        self.areas_of_interest = areas_of_interest
        self.postal_code = postal_code

    def json(self):
        return {"volunteer_id": self.volunteer_id, "volunteer_name": self.volunteer_name, "email": self.email, "age": self.age, "payment": self.payment, "password": self.password,  "skills": self.skills, "username": self.username, "sex": self.sex, "description": self.description, "credentials": self.credentials, "postal_code": self.postal_code, "areas_of_interest": self.areas_of_interest}


# get all volunteers in a list
@app.route("/volunteers")
def get_all_volunteers():
    volunteer_list = Volunteer.query.all()
    if len(volunteer_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "volunteers": [volunteer.json() for volunteer in volunteer_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no registered volunteers."
        }
    ), 404


# create volunteer account
@app.route("/volunteer/add/<int:vid>", methods=['POST'])
def add_volunteer(vid):
    if (Volunteer.query.filter_by(volunteer_id=vid).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "volunteer_id": vid
                },
                "message": "Volunteer already exists."
            }
        ), 400
 
    data = request.get_json()
    volunteer = Volunteer(vid, **data)
 
    try:
        db.session.add(volunteer)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "volunteer_id": vid
                },
                "message": "An error occurred whilst adding the volunteer."
            }
        ), 500
 
    return jsonify(
        {
            "code": 201,
            "data": volunteer.json()
        }
    ), 201


# pull volunteer's personal particulars
@app.route("/volunteer/findById/<int:vid>", methods=['POST'])
def find_by_vid(vid):
    # data = request.get_json()
    # vid = data['volunteer_id']
    volunteer = Volunteer.query.filter_by(volunteer_id=vid).first()
    if volunteer:
        return jsonify(
            {
                "code": 200,
                "data": volunteer.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Volunteer not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)