import sqlite3
# 建立一個 Employee 的資料表
sql = '''
    create table if not exists Employee(
        id integer not null primary key autoincrement,
        e_name text not null,
        e_salary integer
    )
'''
sql = sql.strip()
print(sql)
# 1. 開啟資料庫連線
conn = sqlite3.connect('demo.db')
# 2. 得到 cursor
cursor = conn.cursor()
# 3. 執行 sql 指令
cursor.execute(sql)
# 4. 任務提交
conn.commit()
# 5. 關閉資料庫連線
conn.close()
print('資料表建立完成')

