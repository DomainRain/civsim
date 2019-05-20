import sqlite3

conn = sqlite3.connect('World.db')

c = conn.cursor()

c.execute("SELECT * FROM people")

print(c.fetchall())

conn.commit

conn.close
