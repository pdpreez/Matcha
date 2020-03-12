import sqlite3

conn = sqlite3.connect("dataBase.db") # Stores data here. Creates .db file if does not exist.

# A cursor helps us to execute SQL commands.
c = conn.cursor()

c.execute("""SELECT * FROM `users` WHERE `username`='testman'""")

print(c.fetchall())

conn.commit()

conn.close()