import sqlite3

conn = sqlite3.connect("dataBase.db")
c = conn.cursor()
query = "INSERT INTO `users` (username, email, password) VALUES (?, ?, ?)"
c.execute(query, ("pieter", "test@email.com", "P@ssword1"))
c.execute(query, ("Fizz", "buzz@email.com", "P@ssword1"))
c.execute(query, ("Test", "fake@email.com", "P@ssword1"))
conn.commit()
conn.close()
