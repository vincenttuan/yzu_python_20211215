# 有三組(h, w)資料 170, 50 ; 180, 70 ; 160, 60
h = 170
w = 50
bmi = w / (h/100)**2
print('bmi=', bmi)
if 18 < bmi <= 23:
    print('正常')
else:
    print('不正常')
#-----------------------
h = 180
w = 70
bmi = w / (h/100)**2
print('bmi=', bmi)
if 18 < bmi <= 23:
    print('正常')
else:
    print('不正常')
#-----------------------
h = 160
w = 60
bmi = w / (h/100)**2
print('bmi=', bmi)
if 18 < bmi <= 23:
    print('正常')
else:
    print('不正常')