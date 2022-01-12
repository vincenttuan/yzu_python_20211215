import statistics as stat
'''
python 數組
list = [1, 3, 5, 7, 5] 內容可以重複, 可變更
tuple = (1, 3, 5, 7, 5) 內容可以重複, 不可變更(唯讀)
set = (1, 3, 5, 7) 內容不可以重複
dict = {'name': 'John', 'age':18} key/value元素集合
'''
e1 = {'name':'John', 'salary':50000}
print(e1, e1['name'], e1['salary'])
e2 = {'name':'Mary', 'salary':60000}
e3 = {'name':'Bobo', 'salary':70000}
# 將 3 個 dict 放入 list 數組中
emps = [e1, e2, e3] # 複合數組
# 總薪資
sum = 0
for e in emps:
    sum = sum + e['salary']
print(sum)
# 請問誰的薪資最高 ? 請從 emps 著手
emp_name = ''
max_salary = 0
for e in emps:
    if e['salary'] > max_salary:
        max_salary = e['salary']
        emp_name = e['name']
print(emp_name, max_salary)

# 最高/最低薪資 ?
salary_list = []
for e in emps:
    salary_list.append(e['salary'])
print('所有薪資列表:', salary_list)
print('最高薪資:', max(salary_list))
print('最低薪資:', min(salary_list))

# 求薪資的標準差 ?
avg = stat.mean(salary_list)
sd = stat.stdev(salary_list)
cv = sd / avg
print('薪資平均: %d' % avg)
print('薪資標準差: %.1f' % sd)
print('薪資變異係數: %.2f' % cv)
