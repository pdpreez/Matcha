import sqlite3

conn = sqlite3.connect("dataBase.db") # Stores data here. Creates .db file if does not exist.

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
            `userId`            INT(11) NOT NULL,
            `firstName`         TINYTEXT NOT NULL,
            `lastName`          TINYTEXT NOT NULL,
            `gender`            BOOL NOT NULL,
            `age`               INT(2) NOT NULL,
            `preference`        INT(3) NOT NULL,
            `fame`              INT(5) NOT NULL DEFAULT 0
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `interests` (
            `id`                INT(11) PRIMARY KEY NOT NULL,
            `interest`          TINYTEXT NOT NULL
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `images` (
            `userId`            INT(11) PRIMARY KEY NOT NULL,
            `imageName`         TINYTEXT NOT NULL
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `matches` (
            `userA`             INT(11) NOT NULL,
            `userB`             INT(11) NOT NULL
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `blocked` (
            `blockerId`         INT(11) NOT NULL,
            `blockedId`         INT(11) NOT NULL
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `location` (
            `id`                INT(11) NOT NULL,
            `latitude`          INT(11) NOT NULL,
            `longitude`         INT(11) NOT NULL,
            `area`              TINYTEXT NOT NULL
            )""")

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS `messages` (
            `id`                INT(11) NOT NULL,
            `senderId`          INT(11) NOT NULL,
            `receivedId`        INT(11) NOT NULL,
            `recieved`          BOOL NOT NULL DEFAULT 0
            )""")

conn.commit()

conn.close()