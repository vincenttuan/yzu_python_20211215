# 進行結構化處理
# [ {'name': John, 'salary': 45000}, {'name': Mary, 'salary': 55000} ... ]
# 目的是為了容易分析
file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
employees = []
for row in rows:
    row = row.strip('\n')
    data = row.split(',')
    name = data[0]  # 員工姓名
    salary = int(data[1])  # 員工薪資
    employee = {'name': name, 'salary': salary}  # dict/json 字典格式
    employees.append(employee)

print(employees)
