import sqlite3
import bcrypt   # Used for hashing the password.
from uuid import uuid4  # Used for email verification.
from flask import Flask, json, Response, request
from validators import FormValidator as FV
from Handlers import User
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    return "Welcome to Matcha"


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    response = {"error": []}
    if username is None or FV.FieldOutOfRange(username, 3, 32):
        response["error"] += ("Username out of range",)
    if email is None or FV.FieldTooLong(email, 32):
        response["error"] += ("Email required",)
    if FV.EmailInvalid(email):
        response["error"] += ("Invalid email",)
    if password is None:
        response["error"] += ("Password is required",)
    if not FV.PasswordValid(password):
        response["error"] += ("Invalid password",)
    user = User()
    if user.user_exists(email):
        response["error"] += ("email taken",)
    if response["error"] is not None:
        return response, 409
    else:
        user = User()
        user.email = email
        user.username = username
        user.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        """
        The variable 'password' needs to be encoded in "utf-8" in order for hashing with bcrypt to work in Python 3.
        With Python 3, strings are, by default, unicode strings.
        else: TypeError: Unicode-objects must be encoded before hashing.
        """
        user.verified = 0
        user.verificationKey = uuid4()
        #send email here
        return response, 201


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = User()
    #response = {}
    user.get_user_by_email(email)
    if user.password_correct(password.encode("utf-8")):
        response = app.make_response(({"errors":""}, 200))
        response.set_cookie("user", email)
        # #set cookie here
        print("test")
        #user.get_profile()
        return response, 200
    else:
        return {"errors": "login failed"}, 409


@app.route("/cookie", methods=["GET", "DELETE"])
def authorise():
    if request.method == "GET":
        cookie = request.cookies.get("user")
        user = request.args.get("email")
        if cookie == user:
            return "Yes cookie", 200
        else:
            return "No cookie", 409
    elif request.method == "DELETE":
        response = app.make_response(({"errors":""}, 200))
        response.set_cookie("user", expires=0)
        return response


@app.route("/verify", methods=["GET"])
def verify():
    email = request.args.get("email")
    key = request.args.get("key")
    user = User()
    user.get_user_by_email(email)
    if user.verify_user(key):
        return 200
    else:
        return 409
