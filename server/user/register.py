from server.db import db_service
import re, os, bcrypt


def register(user_data):
    is_user_data_valid = validate_user_data(user_data)
    if is_user_data_valid == True:
        db_response = insert_user_to_db(user_data)
        if type(db_response) == int:
            return {
                "message": f"user register successful for {user_data['first_name']} {user_data['last_name']}",
                "user_id": db_response,
            }, 200
        else:
            return {"message": db_response}, 400

    else:
        return is_user_data_valid, 400


def insert_user_to_db(user):
    if os.getenv("DB_TYPE") == "mysql":
        insert_user_query = "INSERT INTO USERS (EMAIL, USER_NAME, MOBILE, CREDENTIALS) VALUES (%s, %s, %s, %s)"
    else:
        insert_user_query = "INSERT INTO USERS (EMAIL, USER_NAME, MOBILE, CREDENTIALS) VALUES (?, ?, ?, ?)"

    insert_user_data_params = []
    insert_user_data_params.extend(
        [user["email"], f'{user["first_name"]} {user["last_name"]}', user["mobile"]]
    )
    salt = bcrypt.gensalt(10)
    hashed_password = bcrypt.hashpw(user["password"].encode("utf8"), salt)
    insert_user_data_params.append(hashed_password)
    db_res = db_service(insert_user_query, insert_user_data_params)
    if "error" in db_res:
        return db_res["error"]
    else:
        return db_res.lastrowid


def validate_user_data(user):
    mandatory_fields = [
        "email",
        "mobile",
        "first_name",
        "last_name",
        "password",
        "confirm_password",
    ]
    mandatory_flag = list(
        filter(lambda x: x not in list(user.keys()), mandatory_fields)
    )
    if mandatory_flag:
        return f"Please fill the mandatory fields {', '.join(mandatory_flag)}"
    if not validate_email(user["email"]):
        return f'The email {user["email"]} is invalid'
    if not validate_mobile(user["mobile"]):
        return f'The mobile number {user["mobile"]} is invalid'
    if not validate_name(user["first_name"]):
        return f'The firstname {user["first_name"]} is invalid'
    if not validate_name(user["last_name"]):
        return f'The lastname {user["last_name"]} is invalid'
    if validate_name(user["first_name"]) and validate_name(user["last_name"]):
        if not (
            (len(user["first_name"]) <= 2 and len(user["last_name"]) >= 2)
            or (len(user["last_name"]) <= 2 and len(user["first_name"]) >= 2)
        ):
            return "Please enter the proper firstname and lastname"
    if user["password"] != user["confirm_password"]:
        return "password and confirm password mismatch"

    password_validation = validate_password(user["password"])
    cpassword_validation = validate_password(user["confirm_password"])
    if password_validation != True:
        return password_validation["error_message"]
    if cpassword_validation != True:
        return cpassword_validation["error_message"]
    return True


def validate_email(email_id):
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.fullmatch(regex, email_id)


def validate_mobile(mobile_number):
    rule = re.compile(r"^\+?(44)?(0|9)\d{9,13}$")
    return rule.search(mobile_number)


def validate_name(name):
    if name.isnumeric():
        return False
    if " " in name:
        return False
    if name.isalnum():
        return True


def validate_password(password):
    rule = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{8,20}$")
    match = re.search(rule, password)
    if not match:
        return {"error_message": "Password does not meet criteria"}
    return True


# user = {
#     "email": "abcd@gmail.com",
#     "mobile": "0000000000",
#     "first_name": "Rajesh",
#     "last_name": "K",
#     "password": "rajesh@123",
#     "confirm_password": "rajesh@123",
# }
