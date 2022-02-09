import sqlite3
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = "delete from employee where id=%d"
sql = sql.strip() % (5)
print(sql)

cursor.execute(sql)
print('row count:', cursor.rowcount)
conn.commit()
conn.close()
