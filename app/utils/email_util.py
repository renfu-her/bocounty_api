from flask import current_app
import smtplib
from dataclasses import dataclass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.utils.jwt_util import jwt_encode
from uuid import uuid4
import os


def send_verify_email(student_id: str):
    verify_code = jwt_encode({
        "school_id": student_id
    })

    host: str = current_app.config["MAIL_HOST"]
    port: int = current_app.config["MAIL_PORT"]
    password: str = current_app.config["MAIL_PASSWORD"]

    # initial email setting
    email = build_email(student_id, verify_code)
    with smtplib.SMTP(host="smtp.gmail.com", port=port) as smtp:  # 設定SMTP伺服器
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login(host, password)  # 登入寄件者gmail
        smtp.send_message(email)  # 寄送郵件


def build_email(student_id: str, code: str) -> MIMEMultipart:
    email = MIMEMultipart()
    email["subject"] = "Bocountry 驗證信件"
    email["from"] = "Bocountry@noreply.me"
    email["to"] = (current_app.config["MAIL_PATTERN"] % student_id)

    email.attach(payload=build_html(code))
    return email


def build_html(code) -> MIMEText:
    file_name = "./template/email.html"
    html = ""
    with open(file_name, "r", encoding="UTF-8") as f:
        html = f.read()

    # html = html.replace("{{ user_name }}", user_name)
    html = html.replace("{{ host }}", current_app.config["MAIL_VERIFY_HOST"])
    html = html.replace("{{ code }}", code)
    return MIMEText(html, 'html', 'utf-8')
