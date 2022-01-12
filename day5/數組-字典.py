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

