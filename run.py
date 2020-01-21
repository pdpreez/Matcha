import sqlite3
import bcrypt   # Used for hashing the password.
from uuid import uuid4  # Used for email verification.
from flask import Flask, json, Response, request
from validators import FormValidator as FV
from Handlers import User
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    return "Welcome to matcha"


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
    response = {}
    user.get_user_by_email(email)
    if user.password_correct(password.encode("utf-8")):
        #set cookie here
        user.get_profile()
        return response, 200
    else:
        return {"errors": "login failed"}, 409
