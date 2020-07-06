import sqlite3

conn = sqlite3.connect("dataBase.db")
c = conn.cursor()
query = "INSERT INTO `interests` (interest) VALUES (?)"
tagFile = open("tags", 'r')
tagList = []
for tag in tagFile:
	tag = tag.strip()
	c.execute(query, (tag,))
	conn.commit()
conn.close()
tagFile.close
# Reads from the "tags" file.