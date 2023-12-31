from uuid import uuid4
from app.database.model.chatroom import ChatroomStatus


def format_create_payload(order_id: str):
    payload: dict = dict()

    payload['id'] = uuid4().hex
    payload['order_id'] = order_id
    payload['status'] = ChatroomStatus.RECRUITING.value

    return payload
