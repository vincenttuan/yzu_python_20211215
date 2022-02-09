import sqlite3
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = "update employee set e_name='%s', e_salary=%d where id=%d"
sql = sql.strip() % ('Helen', 55000, 5)
print(sql)

cursor.execute(sql)
print('row count:', cursor.rowcount)
conn.commit()
conn.close()
