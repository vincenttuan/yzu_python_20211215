import sqlite3
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = '''
    insert into Employee(e_name, e_salary)
    values('%s', %d)
'''
sql = sql.strip() % ('Bobo', 45000)
print(sql)

cursor = cursor.execute(sql)
print('insert record rowcount:', cursor.rowcount)
print('last row id:', cursor.lastrowid)
conn.commit()
conn.close()
