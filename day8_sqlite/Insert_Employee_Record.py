import sqlite3
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = '''
    insert into Employee(e_name, e_salary)
    values('%s', %d)
'''
sql = sql.strip() % ('Joanna', 105000)
print(sql)

cursor = cursor.execute(sql)
print('insert record rowcount:', cursor.rowcount)
conn.commit()
conn.close()
