from server.db import db_service
from flask_jwt_extended import create_access_token
from flask import jsonify
import bcrypt


def login(email, password):
    verify_query = "SELECT USER_NAME, EMAIL, CREDENTIALS FROM USERS WHERE EMAIL = ?"
    verify_query_params = []
    verify_query_params.append(email)
    user_details = db_service(verify_query, verify_query_params).fetchone()
    hashed_credentials = user_details[2]
    is_credentials_match = bcrypt.checkpw(password.encode("utf8"), hashed_credentials)
    if not user_details or (user_details and not is_credentials_match):
        return "username or password is incorrect", 403
    else:
        access_token = create_access_token(identity=email)
        return {
            "Token": access_token,
            "message": f"login successful for user {user_details[0]}",
        }, 200
