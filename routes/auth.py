from flask import Blueprint, abort, request, jsonify
from database import *
from functools import wraps
import jwt
import hashlib
import json

auth_bp = Blueprint("auth", __name__)
SECRET_KEY = "5649fa3d35bb66267f46b5d0027e67fd"

# Code for jwt authentication from
# https://www.bacancytechnology.com/blog/flask-jwt-authentication
# 10/29/2022


def hash_password(password):
    password = password.encode()
    password_hash = hashlib.sha224(password)
    return password_hash.digest().hex()


@auth_bp.route("/login", methods=["POST"])
def login():
    login_info = json.loads(request.data)
    email = login_info["email"]
    password = login_info["password"]
    password_hash = hash_password(password)
    print(password_hash)
    login_response = login_user(email, password_hash)
    if login_response == 1:
        return "Email or password incorrect", 400
    else:
        print(login_response)
        token = jwt.encode(
            {
                "userId": login_response[0],
                "username": login_response[1],
                "avatar": login_response[2],
            },
            SECRET_KEY,
            "HS256",
        )
        return json.dumps({"token": token})


@auth_bp.route("/register", methods=["POST"])
def register():
    registration_info = json.loads(request.data)
    print(registration_info)
    username = registration_info["username"]
    password_a = registration_info["passwordA"]
    password_b = registration_info["passwordB"]
    email = registration_info["email"]
    if password_b != password_a:
        return "Passwords not equal", 400
    else:
        password_hash = hash_password(password_b)
        registration_response = register_user(username, password_hash, email)
        if registration_response == 1:
            return "Email in use", 400
        token = jwt.encode(
            {
                "userId": registration_response[0],
                "username": registration_response[1],
                "avatar": registration_response[2],
            },
            SECRET_KEY,
            "HS256",
        )
        return json.dumps({"token": token})


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if "access-token" in request.headers:
            token = request.headers["access-token"]
        if not token:
            return jsonify({"message": "a valid token is missing"})
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return f(str(data["userId"]), *args, **kwargs)

    return decorator
