from flask import Flask, json, Response, request
from validators import FormValidator as FV
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    return "Welcome to matcha"


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    if username is None or FV.FieldOutOfRange(username, 3, 32):
        return {"error": "Username must be between 3 and 32 characters"}, 409
    if email is None or FV.FieldTooLong(email, 32):
        return {"error": "Email required"}, 409
    if FV.EmailInvalid(email):
        return {"error": "Invalid Email"}, 409
    if password is None:
        return {"error": "Password is required"}, 409
    if FV.PasswordValid(password):
        return {"error": ""}, 200
    else:
        return {"error": "Invalid password"}, 409


@app.route("/login")
def login():
    data = {"errors": ""}
    return data, 200
