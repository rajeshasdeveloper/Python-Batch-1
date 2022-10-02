from app import app
from flask import request, make_response, jsonify
from server.user.register import register
from server.user.login import login
from server.user.user_detail import get_user_details
from server.user.update_user import update_user_details
from flask_jwt_extended import jwt_required

from server.db import validate_database
import os

os.environ["DB_TYPE"] = "sqlite3"
validate_database()
# from templates.home import home


@app.route("/")
def home_route():
    result = {"message": "Welcome You are in a Flask app"}
    return make_response(jsonify(result))


@app.route("/user/login", methods=["POST"])
def login_user():
    print(request.get_json())
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    login_response, status_code = login(email, password)
    return make_response(login_response, status_code)


@app.route("/user/register", methods=["POST"])
def register_user():
    user_data = request.get_json()
    signup_response, status_code = register(user_data)
    return make_response(signup_response, status_code)


@app.route("/user/profile/update", methods=["POST"])
def update_user_profile():
    user_data = request.get_json()
    update_response, status = update_user_details(user_data)
    return make_response(update_response, status)


@app.route("/user/details")
@jwt_required()
def user_details():
    return get_user_details(request.args.get("email"))
