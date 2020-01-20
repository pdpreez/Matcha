import sqlite3
import bcrypt

class User:

    def __init__(self):
        self.id = None
        self.username = None
        self.email = None
        self.password = None
        self.verified = None
        self.verificationKey = None
        self.reported = None
        self.firstname = None
        self.lastname = None
        self.gender = None
        self.dob = None
        self.sexuality = None
        self.fame = None
        self.interests = []
        self.dbconn = sqlite3.connect("./Database/dataBase.db")
        self.dbconn.row_factory = sqlite3.Row
        self.cursor = self.dbconn.cursor()

    def user_exists(self, email):
        query = "SELECT count(*) FROM `users` WHERE `email`=?"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchall()
        if result[0][0] > 0:
            return True
        else:
            return False

    def get_user_by_email(self, email):
        query = "SELECT * FROM `users` WHERE `email`=?"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchall()
        for item in result:
            self.id = item["id"]
            self.username = item["username"]
            self.email = item["email"]
            self.password = item["password"]
            self.verified = item["verified"]
            self.verificationKey = item["verificationKey"]
            self.reported = item["reported"]

    def get_profile(self):
        query = "SELECT * FROM `profile` WHERE `userId`=?"
        self.cursor.execute(query, (self.id,))
        result = self.cursor.fetchall()
        for item in result:
            print(dict(item))

    def get_user_by_username(self, username):
        query = "SELECT * FROM `users` WHERE `username`=?"
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchall()
        for item in result:
            self.id = item["id"]
            self.username = item["username"]
            self.email = item["email"]
            self.password = item["password"]
            self.verified = item["verified"]
            self.verificationKey = item["verificationKey"]
            self.reported = item["reported"]

    def password_correct(self, password):
        if bcrypt.checkpw(password, self.password):
            return True
        else:
            return False
