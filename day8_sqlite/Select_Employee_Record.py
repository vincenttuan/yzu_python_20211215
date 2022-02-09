import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
sql = 'select id, e_name, e_salary from employee'
cursor.execute(sql)
rows = cursor.fetchall()  # 得到所有回傳紀錄
# 顯示資料
for row in rows:
    print(row[0], row[1], row[2])
conn.close()
