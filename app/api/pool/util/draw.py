from random import randint
from app.database.util import update, get, create
from app.utils.auth.auth_util import get_login_user
from app.utils.time_util import get_current, date2str
from app.database.model.account import (
    get_account_by_student_id,
    update_account_by_id
)
from .pool import PoolItem

from flask import request

from .pool import DrawType
from .get import get_pool_item


def draw_card(pool_id:str):
    payload: dict = request.json
    type = payload["type"]


    item_list = get_pool_item(pool_id)

    num = 0
    print(type, DrawType.multi.value)
    if type == DrawType.single.value:
        num = 1
    elif type == DrawType.multi.value:
        num = 10


    user = get_login_user()
    update_account_by_id(user["id"], {"bocoin":user.get("bocoin") - (10 * num) })

    res = []
    print(item_list)
    for i in range(num):
        picked = 0
        if len(item_list) > 1:
            picked = randint(0, len(item_list) - 1)

        res.append(item_list[picked])
    print(num, res)

    update_item(res)

    return convert_item(res)

def convert_item(itemList: list[PoolItem]):
    res = []
    for i in itemList:
        res.append(get("item",{
            "id":i.item_id
        })[0])
    return res

def update_item(item_list: list[PoolItem]):
    user = get_login_user()
    current = date2str(get_current())

    for item in item_list:
        items = get('own_item', {
            "user_id": user.get('id'),
            "item_id": item.item_id
        })

        if len(items) != 0:
            continue

        create('own_item', {
            "user_id": user.get('id'),
            "item_id": item.item_id,
            "time": current
        })
