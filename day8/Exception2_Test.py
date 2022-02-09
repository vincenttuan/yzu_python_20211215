a = 10
b = [2, 0]
# ZeroDivisionError 除以0的錯誤
# IndexError: list index out of range
try:
    c = a / b[0]
    # 其他程序 ...
except ZeroDivisionError as e:
    print('數學錯誤發生:', e, e.__class__)
except IndexError as e:
    print('Index錯誤發生:', e, e.__class__)
except:
    print('其他錯誤發生')
else:
    print(c)
