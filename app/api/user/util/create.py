from app.database.util import create
from app.utils.time_util import get_current, date2str
from flask import request, current_app, Flask
from app.utils.email_util import send_verify_email
import threading


def create_user():
    payload: dict = request.json
    create("account", payload)

    user_id = payload.get('id')
    current_time = date2str(get_current())
    item_ids = [
        "6fbd9679bd8b41239f584624af23e74b",
        "0b7e63b98e0143e980bd3c2c3e815f73",
        "820c69b5e95b40c5bf121a337a1f1cec",
        "e196fbb8fd934a9cbfd5d968c3dae18a",
        "4d5d21b000bf4a29bdb9c35c00d7da6d",
        "d15ca4c26e3b469083e697dd249b75ca"
    ]

    for item_id in item_ids:
        create("own_item", {
            "user_id":user_id,
            "item_id":item_id,
            "time": current_time
        })

    for item_id in item_ids[:3]:
        create("picked_item", {
            "user_id": user_id,
            "item_id": item_id,
        })

    if current_app.config["MAIL_ENABLE"]:
        thread = FlaskThread(
            target=send_verify_email, args=[payload.get('student_id')])
        thread.start()


class FlaskThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # type: ignore[attr-defined]
        self.app: Flask = current_app._get_current_object()

    def run(self) -> None:
        with self.app.app_context():
            super().run()
