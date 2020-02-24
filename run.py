import sqlite3
import bcrypt   # Used for hashing the password.
import requests # To call other APIs, specifically for geolocation
from uuid import uuid4  # Used for email verification.
from flask import Flask, json, Response, request, session
from flask_cors import CORS, cross_origin
from validators import FormValidator as FV
from Handlers import User
#import insert
#import vermail

geoAPI = "http://ip-api.com/json/"

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.secret_key = "SECRET"


@app.route("/", methods=["GET", "POST"])
def root():
    return "Welcome to Matcha"


@app.route("/register", methods=["POST"])
def register():
    req = json.loads(request.data.decode())
    print(req)
    username = req["username"]
    email = req["email"]
    password = req["password"]
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
    if len(response["error"]) > 0:
        print(response)
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
        user.verificationKey = str(uuid4().time_low) # Converts uuid to int, then to string, so it's stored correctly in the database
        # Add user to database here.
        user.save_user()
        #send email here
        #verMail(user.email, user.verificationKey)
        return response, 201


@app.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login():
    req = json.loads(request.data.decode())
    email = req["email"]
    password = req["password"]
    user = User()
    response = {}
    user.get_user_by_email(email)
    if user.password_correct(password.encode("utf-8")):
        response = app.make_response(({"errors": ""}, 200))
        response.set_cookie("user", email, secure=True)
        session["user"] = email
        # #set cookie here
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
        response = app.make_response(({"errors": ""}, 200))
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


@app.route("/profile", methods=["GET"])
def profile():
    email = request.args.get("email")
    user = User()
    user.get_user_by_email(email)
    user.get_profile()
    print(user.gender)
    resp = app.make_response(("response", 200))
    return resp


@app.route("/locate", methods=["GET"])
def locate():
    ip_addr = request.remote_addr
    email = request.args.get("email")
    user = User()
    user.get_user_by_email(email)
    r = requests.get(geoAPI)
    r = json.loads(r.text)
    user.latitude = r["lat"]
    user.longitude = r["lon"]
    user.city = r["city"]
    return ip_addr, 200

if __name__ == '__main__':
    app.run(debug=True)