import sqlite3
import bcrypt
from validators import FormValidator as FV


class User:

    def __init__(self):
        self.id = None                  # Automatically added
        self.username = None
        self.email = None
        self.password = None
        self.verified = None            # [0] - no; 1 - yes
        self.verificationKey = None     # [0]
        self.reported = None            # 0 - no; 1 - yes
        self.firstname = None
        self.lastname = None
        self.gender = None              # 0 - f; 1 - m
        self.age = None                 # 18 - 100 only
        self.sexuality = None           # 0 - f; 1 - m; [2] - fm
        self.fame = None                # [0] - 5
        self.latitude = None
        self.longitude = None
        self.city = None
        self.interests = []
        self.dbconn = sqlite3.connect("./Database/dataBase.db")
        self.dbconn.row_factory = sqlite3.Row
        self.cursor = self.dbconn.cursor()

    # Checks to see if the email has been taken.
    def user_exists(self, email, username):
        query = "SELECT count(*) FROM `users` WHERE `email`=? OR `username`=?"
        self.cursor.execute(query, (email, username,))
        result = self.cursor.fetchall()
        if result[0][0] > 0:
            return True
        else:
            return False

    # Gets the user by email.
    def get_user_by_email(self, email):
        query = "SELECT * FROM `users` WHERE `email`=?"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchall()
        if result:
            for item in result:
                self.id = item["id"]
                self.username = item["username"]
                self.email = item["email"]
                self.password = item["password"]
                self.verified = item["verified"]
                self.verificationKey = item["verificationKey"]
                self.reported = item["reported"]

    # Get a user's profile.
    def get_profile(self):
        query = "SELECT * FROM `profile` WHERE `userId`=?"
        self.cursor.execute(query, (self.id,))
        result = self.cursor.fetchall()
        if len(result) > 0:
            for item in result:
                print("get_profile")
                print(item)
        else:
            print("boo")

    # Get a user by their username.
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

    # Inserts the user's details upon registration.
    def save_user(self):
        # Adding to users.
        query = "INSERT INTO `users`(username, email, password, verificationKey) VALUES(?, ?, ?, ?)"
        self.cursor.execute(query, (self.username, self.email, self.password, self.verificationKey))
        self.dbconn.commit()
        # Getting the user id (This is in case of Dummyusers.py being run or any 
        # other programme to automatically add users to the database).
        query = "SELECT * FROM `users` WHERE `username`=?"
        self.cursor.execute(query, (self.username,))
        result = self.cursor.fetchall()
        for item in result:
            self.id = item["id"]
        # Adding to profile.
        query = "INSERT INTO `profile`(userId, firstName, lastName, gender, age, bio) VALUES(?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (self.id, self.firstname, self.lastname, self.gender, self.age, ""))
        self.dbconn.commit()

    # Checks to see if the password is correct on login.
    def password_correct(self, password):
        if bcrypt.checkpw(password, self.password):
            return True
        else:
            return False

    # Verifys the user.
    def verify_user(self, verificationKey):
        if not self.verified:
            if self.verificationKey == verificationKey:
                self.verified = True
                query = "UPDATE `users` SET `verified`=TRUE WHERE `id`=?"
                self.cursor.execute(query, (self.id,))
                self.dbconn.commit()
                return True
            else:
                return False

    # Update user's email.
    def update_email(self, new_email, username):
        query = "SELECT count(*) FROM `users` WHERE `email`=?"
        self.cursor.execute(query, (new_email,))
        result = self.cursor.fetchall()
        if result[0][0] > 0:
            return False
        else:
            query = "UPDATE `users` SET `email`=? WHERE `username`=?"
            self.cursor.execute(query, (new_email, self.username))
            self.dbconn.commit()
            return True

    # Update user's password.
    def update_password(self, new_password):
        if FV.PasswordValid(new_password):
            query = "UPDATE `users` SET `password`=? WHERE `id`=?"
            hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt())
            self.cursor.execute(query, (hashed, self.id))
            self.dbconn.commit()
            return True
        else:
            return False

    # >>>> Update user's firstname.
    def update_firstname(self, new_firstname):
        if FV.FieldOutOfRange(new_firstname, 3, 32):
            return False
        else:
            query = "UPDATE `profile` SET `firstname`=? WHERE `userId`=?"
            self.cursor.execute(query, (new_firstname, self.id))
            return True

    # >>>> Update user's lastname.
    def update_lastname(self, new_lastname):
        if FV.FieldOutOfRange(new_lastname, 3, 32):
            return False
        else:
            query = "UPDATE `profile` SET `lastname`=? WHERE `userId`=?"
            self.cursor.execute(query, (new_lastname, self.id))
            return True

    # >>>> Update user's age.
    def update_age(self, new_age):
        if new_age > 17:
            query = "UPDATE `profile` SET `age`=? WHERE `userId`=?"
            self.cursor.execute(query, (new_age, self.id))
            return True
        else:
            return False

    # Update user's preference.
    def update_preference(self, new_preference):
        if new_preference > -1 and new_preference < 3:
            query = "UPDATE `profile` SET `preference`=? WHERE `userId`=?"
            self.cursor.execute(query, (new_preference, self.id))
            self.dbconn.commit()
            return True
        else:
            return False
    
    # Update user's bio.
    def update_bio(self, new_bio):
        try:
            query = "UPDATE `profile` SET `bio`=? WHERE `userId`=?"
            self.cursor.execute(query, (new_bio, self.id))
            self.dbconn.commit()
            return True
        except:
            return False

    # Update user's location.
    def update_location(self):
        if len(city) != 0:
            query = "UPDATE `location` SET `lat`=?, `lon`=?, `area`=? WHERE `id`=?"
            self.cursor.execute(query, (self.latitude, self.longitude, self.city, self.id))
            return True
        else:
            return False

    # Add locaation.
    def add_location(self):
        if len(city) != 0:
            query = "INSERT INTO `location` VALUES (?, ?, ?, ?)"
            self.cursor.execute(query, (self.id, self.latitude, self.longitude, self.city))
            return True
        else:
            return False

    # Add tag to user's profile.
    def add_tag(self, tagId):
        query = "SELECT count(*) FROM `userInterests` WHERE `userId`=? AND `interestID`=?"
        self.cursor.execute(query, (self.id, tagId))
        result = self.cursor.fetchall()
        if result[0][0] > 0:
            return False
        else:
            query = "INSERT INTO `userInterests` (userId, interestID) VALUES (?, ?)"
            self.cursor.execute(query, (self.id, tagId))
            self.dbconn.commit()
            return True
        
    # Remove tag from user's profile.
    def remove_tag(self, tagId):
        query = "SELECT count(*) FROM `userInterests` WHERE `userId`=? AND `interestID`=?"
        self.cursor.execute(query, (self.id, tagId))
        result = self.cursor.fetchall()
        if result[0][0] > 0:
            query = "DELETE FROM `userInterests` WHERE `userId`=? AND `interestID`=?"
            self.cursor.execute(query, (self.id, tagId))
            self.dbconn.commit()
            return True
        else:
            return False

    def save_profile(self):
        query = "INSERT INTO `profile` (userId, firstName, lastName, gender, age) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (self.id, self.firstname, self.lastname, self.gender, self.age))
        self.dbconn.commit()