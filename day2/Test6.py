# print 輸出
age, name = '18', 'John'
print(age + '歲的' + name)

age, name = 18, 'John'
print(str(age) + '歲的' + name)

print(age, end='')
print('歲的', end='')
print(name)

print('台積電', 610, 5000, sep=',')
