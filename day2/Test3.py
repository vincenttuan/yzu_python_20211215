# 轉型(變態 = 改變資料型/別) Lab
#h = "170.0"
#w = '60.5'
h = input('請輸入身高: ')
w = input('請輸入體重: ')
# 請計算 bmi = ?
try:
    h = float(h) / 100  # 公尺
    w = float(w)
    bmi = w / h**2
    print(bmi)
except:
    print('資料輸入不正確')
