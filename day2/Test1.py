# python 保留字
import keyword
print(keyword.kwlist)

# 變數的賦值
a = b = c = 100
print(a, b, c)

age, name = 18, "John"
print(age, name)
# 變數的資料類型(型態)
print(type(age), type(name))

# 浮點數
a = 3.14
b = 3.14e2 # 科學記號 3.14 * 100
print(a, b)
print(type(a), type(b))

# 綜合練習
a, b, c, d = 10, 20.5, True, 'Mary'
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

# 刪除變數
print("a =", a)
del a
#print("a =", a) # a 變數刪除後就不可以使用
