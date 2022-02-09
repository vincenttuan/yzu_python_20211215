a = 10
b = [2, 0]
# ZeroDivisionError 除以0的錯誤
# IndexError: list index out of range
try:
    c = a / b[2]
except Exception as e:
    print('有錯誤發生:', e, e.__class__)
else:
    print(c)
