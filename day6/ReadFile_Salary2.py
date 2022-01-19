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
# Lab 請求出薪資總合與平均 = ?
sum = 0
for employee in employees:
    #print(employee['salary'], type(employee['salary']))
    sum = sum + employee['salary']
avg = sum / len(employees)
print('薪資總合: %d、薪資平均: %.1f' % (sum, avg))

# 將計算結果寫入檔案
result = '薪資總合: %d、薪資平均: %.1f' % (sum, avg)
file = open('result.txt', 'w', encoding='UTF-8')
file.write(result)
file.close()
print('寫入檔案完成')
