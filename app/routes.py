from copyreg import constructor
from app import app
from flask import request, make_response, jsonify
from server.user.register import register

from server.db import validate_database

validate_database()
# from templates.home import home


# @app.route("/", methods=["POST", "GET"])
# def home_route():
#     if request.method == "GET":
#         result = {"message": "Welcome You are in a Flask app"}
#     else:
#         result = request.get_json()
#         result = result or request.args
#     return make_response(jsonify(result))


@app.route("/user/login")
def login_user():
    pass


@app.route("/user/register", methods=["POST"])
def register_user():
    user_data = request.get_json()
    signup_response, status_code = register(user_data)
    return make_response(signup_response, status_code)
