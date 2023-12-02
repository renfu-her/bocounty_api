from flask import Blueprint, request,current_app, Flask
from app.database.model.account import (
    get_account_by_student_id,
    update_account_by_id
)
from app.utils.response import success
from app.utils.auth.auth_util import required_login
from app.utils.jwt_util import  jwt_decode


verify_page = Blueprint("verify_page", __name__, url_prefix="/page/verify")


@verify_page.route("/<string:verifyToken>")
def get_detail(verifyToken: str):
    try:
        payload = jwt_decode(verifyToken)
        user = get_account_by_student_id(payload["school_id"])
        print(user)
        if(user is None) or (user.verify == 1):
            raise Exception()
        update_account_by_id(user.id,{
            "verify": 1
        })

    except Exception as e:
        print(e)
        return "fail"
    return "success"
