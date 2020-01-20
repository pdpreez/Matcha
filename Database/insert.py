import sqlite3

conn = sqlite3.connect("dataBase.db") # Stores data here. Creates .db file if does not exist.

# A cursor helps us to execute SQL commands.
c = conn.cursor()

# Creates test user. Note that the password is not yet hashed.
c.execute("""INSERT INTO `users` (`username`, `email`, `password`) VALUES (
			'testman',
			'test@test.com',
			'G00dPass')""")

conn.commit()

conn.close()