import sqlite3
from Handlers import User

conn = sqlite3.connect("dataBase.db")
c = conn.cursor()

# Searches the database to see if the user exists.
def dupicateCheck(username, email):
    query = "SELECT * FROM `users` WHERE `username` = ? OR `email` = ? LIMIT 1"
    c.execute(query, (username, email,))
    res = c.fetchone()
    conn.commit()
    if not res:
        return response, 202 # Accepted
    else:
        return response, 409 # Conflict

# Inserts a user into the databse.
def insertUser(username, email, password):
    query = "INSERT INTO `users` (`username`, `email`, `password`) VALUES (?, ?, ?)"
    c.execute(query, (username, email, password))
    conn.commit()

conn.close()