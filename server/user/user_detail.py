from server.db import db_service


def get_user_details(email):
    user_detail_query = (
        "SELECT USER_ID, EMAIL, USER_NAME, MOBILE FROM USERS WHERE EMAIL=?"
    )
    user_detail_query_param = []
    user_detail_query_param.append(email)
    user_detail = db_service(user_detail_query, user_detail_query_param).fetchone()
    if user_detail:
        return {
            "user_id": user_detail[0],
            "email_id": user_detail[1],
            "user_name": user_detail[2],
            "mobile": user_detail[3],
        }, 200
    else:
        return "User not found for enetered email", 404
