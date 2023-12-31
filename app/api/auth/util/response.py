from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify


def wrong_format():
    raise HTTPException(response=make_response(jsonify({
        "message": "wrong format"
    }), 400))


def missing_required():
    raise HTTPException(response=make_response(jsonify({
        "message": "missing required column"
    }), 400))


def incorrect():
    raise HTTPException(response=make_response(jsonify({
        "message": "incorrect student id or password"
    }), 401))


def not_verified():
    raise HTTPException(response=make_response(jsonify({
        "message": "user no verified"
    }), 403))
