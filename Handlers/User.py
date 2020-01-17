import sqlite3


class User:

    def __init__(self):
        username = None
        firstname = None
        lastname = None
        email = None
        gender = None
        dob = None
        sexuality = None
        fame = None
        interests = []

    def get_user_by_email(self, email):
        #ask DB for email
        pass

    def getUserByUsername(self, username):
        #ask DB for username
        pass

    def populateProfile(self, profile):
        for item in profile:
            pass