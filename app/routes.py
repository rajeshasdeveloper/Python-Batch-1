from crypt import methods
from app import app
from flask import request, make_response, jsonify
from templates.home import home


@app.route("/", methods=["POST", "GET"])
def home_route():
    if request.method == "GET":
        result = {"message": "Welcome You are in a Flask app"}
    else:
        result = request.get_json()
        result = result or request.args
    return make_response(jsonify(result))


@app.route("/users")
def get_users():
    pass

@app.route('/users/register', methods=["POST"])
def register_user():
    body_data = request.get_json()
    
