import sqlite3
con = sqlite3.connect('data.db')

cur = con.cursor()
cur.execute('SELECT * FROM companies')
rows = cur.fetchall()

for rows in rows:
    print(rows)


