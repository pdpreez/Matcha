import sqlite3

conn = sqlite3.connect("dataBase.db") # Stores data here. Creates .db file if does not exist.

conn.execute("PRAGMA foreign_keys = ON") # Enables CASCADE and FOREIGN KEY use.
# ^ There is a small problem with the line above.
# It works when you input it into the sqlite command line programme.

# A cursor helps us to execute SQL commands.
c = conn.cursor()

# The docstring (multiline comment) allows us to write on multiple lines.
# This is done as in the python documentation.
c.execute("""CREATE TABLE IF NOT EXISTS `users` (
            `id`                INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            `username`          TINYTEXT NOT NULL,
            `email`             TINYTEXT NOT NULL,
            `password`          TINYTEXT NOT NULL,
            `verified`          BOOL NOT NULL DEFAULT 0,
            `verificationKey`   TINYTEXT NOT NULL DEFAULT 0,
            `reported`          BOOL NOT NULL DEFAULT 1
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `profile` (
            `userId`            INTEGER NOT NULL,
            `firstName`         TINYTEXT NOT NULL,
            `lastName`          TINYTEXT NOT NULL,
            `gender`            BOOL NOT NULL,
            `age`               INT(2) NOT NULL,
            `preference`        INT(3) NOT NULL,
            `fame`              INT(5) NOT NULL DEFAULT 0,
            FOREIGN KEY (userId) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `interests` (
            `id`                INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            `interest`          TINYTEXT NOT NULL
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `userInterests` (
            `userId`            INTEGER NOT NULL,
            `interestID`        INTEGER NOT NULL,
            FOREIGN KEY (userId) REFERENCES `users` (id) ON DELETE CASCADE,
            FOREIGN KEY (interestID) REFERENCES `interests` (id)
                ON DELETE CASCADE
                ON UPDATE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `images` (
            `userId`            INTEGER NOT NULL,
            `imageName`         TINYTEXT NOT NULL,
            FOREIGN KEY (userId) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `matches` (
            `userA`             INTEGER NOT NULL,
            `userB`             INTEGER NOT NULL,
            `liked`             INTEGER NOT NULL,
            FOREIGN KEY (userA) REFERENCES `users` (id) ON DELETE CASCADE,
            FOREIGN KEY (userB) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `blocked` (
            `blockerId`         INTEGER NOT NULL,
            `blockedId`         INTEGER NOT NULL,
            FOREIGN KEY (blockerId) REFERENCES `users` (id) ON DELETE CASCADE,
            FOREIGN KEY (blockedId) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `location` (
            `id`                INTEGER NOT NULL,
            `latitude`          INT(11) NOT NULL,
            `longitude`         INT(11) NOT NULL,
            `area`              TINYTEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `messages` (
            `id`                INTEGER NOT NULL,
            `senderId`          INT(11) NOT NULL,
            `receivedId`        INT(11) NOT NULL,
            `recieved`          BOOL NOT NULL DEFAULT 0,
            `content`           TINYTEXT NOT NULL,
            FOREIGN KEY (id) REFERENCES `users` (id)
                ON DELETE CASCADE
            )""")
conn.commit()


conn.close()
