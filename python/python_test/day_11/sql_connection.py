import sqlite3 as sqlite

con = sqlite.connect('mydb.db')

cursor = con.cursor()

cursor.execute("select * from product")



