from flask import Response
from datetime import datetime, timedelta, timezone
from app.utils.jwt_util import jwt_encode
import requests


def with_jwt(res: Response, user: dict) -> Response:
    expires = datetime.now(tz=timezone(timedelta(hours=8))) + timedelta(days=2)

    encoded = jwt_encode({
        "id": user["id"],
        "exp": expires
    })

    res.set_cookie('user_token', encoded, expires=expires)

    print(user['id'], user['name'], user['student_id'], user['bocoin'], encoded);

    send_token(user['id'], user['name'], user['student_id'], user['bocoin'], encoded)

    return res


def without_jwt(res: Response) -> Response:
    res.set_cookie('user_token', "", expires=-1)
    return res

def send_token(user_id, name, student_id, bocoin, encoded):
    laravelApiUrl = 'https://demo.dev-laravel.co/api/user_token/check'
    payload = {
        'user_id': user_id, 
        'name': name,
        'student_id': student_id,
        'bocoin': bocoin,
        'user_token': encoded
        }
    print(payload);    
    r = requests.post(laravelApiUrl, json=payload)
