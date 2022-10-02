from server.db import db_service
from .register import validate_email, validate_mobile, validate_name


def update_user_details(user_details):
    user_data = list(map(lambda x: x.upper(), user_details.keys()))
    user_data.remove("FIRST_NAME")
    user_data.remove("LAST_NAME")
    user_data.remove("PASSWORD")
    user_data.remove("CONFIRM_PASSWORD")
    if "email" in user_details:
        is_email_valid = validate_email(user_details["email"])
        if not is_email_valid:
            return f'The email {user_details["email"]} is invalid', 400
    if "first_name" in user_details and "last_name" in user_details:
        user_data.append("USER_NAME")
        is_first_name_valid = validate_name(user_details["first_name"])
        is_last_name_valid = validate_name(user_details["last_name"])
        if not is_first_name_valid or not is_last_name_valid:
            return f"The username is invalid", 400
    if ("first_name" in user_details and "last_name" not in user_details) or (
        "last_name" in user_details and "first_name" not in user_details
    ):
        return "First name and last name are mandatory to update the user name", 400

    if "mobile" in user_details:
        is_mobile_number_valid = validate_mobile(user_details["mobile"])
        if not is_mobile_number_valid:
            return f"The mobile number {user_details['mobile']} is invalid", 400
    user_details[
        "user_name"
    ] = f"{user_details['first_name']} {user_details['last_name']}"
    db_response = update_user_to_db(user_details, user_data)
    if type(db_response) == int and db_response != 0:
        return {
            "message": f"user update successful for {user_details['first_name']} {user_details['last_name']}",
        }, 200
    elif type(db_response) == int and db_response == 0:
        return {
            "message": "user not found",
        }, 404
    else:
        return {"message": db_response}, 400


def update_user_to_db(user, update_list):
    update_user_query = "UPDATE USERS SET"
    update_user_data_params = []
    for update_item in update_list:
        update_user_query += f" {update_item} = ?"
        update_user_data_params.append(user[update_item.lower()])
        if update_list.index(update_item) != len(update_list) - 1:
            update_user_query += ", "
    update_user_query += " WHERE EMAIL = ?"
    update_user_data_params.append(user["email"])
    db_res = db_service(update_user_query, update_user_data_params)
    if "error" in db_res:
        return db_res["error"]
    else:
        return db_res.rowcount
