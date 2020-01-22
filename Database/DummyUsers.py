import sqlite3
import bcrypt

conn = sqlite3.connect("dataBase.db")
c = conn.cursor()
query = "INSERT INTO `users` (username, email, password) VALUES (?, ?, ?)"
prehash = "P@ssword1"
password = bcrypt.hashpw(prehash.encode(), bcrypt.gensalt())
c.execute(query, ("pieter", "test@email.com", password))
c.execute(query, ("Fizz", "buzz@email.com", password))
c.execute(query, ("Test", "fake@email.com", password))
conn.commit()
conn.close()
