from flask import Flask
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS, cross_origin

ACCESS_EXPIRES = timedelta(minutes=20)

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "blueeyes"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
jwt = JWTManager(app)


from app import routes
