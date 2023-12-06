from app.database.util import get
from app.utils.response import not_found, missing_required, wrong_format, not_enough_coin
from app.utils.auth.auth_util import get_login_user
from .pool import DrawType
from flask import request


def validate_pool_itme(pool_id: str):
    _validate_pool_exist(pool_id)


def validate_draw(pool_id: str):
    _validate_payload()
    _validate_pool_exist(pool_id)
    _validate_pool_not_empty(pool_id)
    _validate_coin()


def _validate_payload():
    payload: dict = request.json

    type = payload.get("type")
    print(type)
    if type is None:
        missing_required("type not found")
    if (type != 1) and type != 2:
        wrong_format()


def _validate_pool_exist(pool_id: str):
    pool_list = get('pool', {
        "id": pool_id
    })

    if len(pool_list) != 1:
        not_found('pool not found')


def _validate_pool_not_empty(pool_id: str):
    pool_item_list = get('pool_item', {
        "pool_id": pool_id
    })

    if len(pool_item_list) == 0:
        not_found('pool is empty')


def _validate_coin():
    user = get_login_user()
    user_coin = user.get("bocoin")
    payload: dict = request.json
    type = payload.get("type")

    if (type == DrawType.single.value):
        if (user_coin < 10):
            not_enough_coin()
    else:
        if user_coin < 100:
            not_enough_coin()
