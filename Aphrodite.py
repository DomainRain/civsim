import sqlite3

conn = sqlite3.connect('World.db')

c = conn.cursor()
t = 'propertyiorityStat'
c.execute("SELECT * FROM people WHERE married='none'")
row = c.fetchall()
print(row[5][13])


conn.commit

conn.close
