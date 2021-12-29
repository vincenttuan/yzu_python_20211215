# 有三組(h, w)資料 170, 50 ; 180, 70 ; 160, 60
# 請試做一個 def calcBmi 方法
# calcBmi 方法可以輸入 2 個參數
# 可以印出 bmi 值 與 bmi 是否正常 (18<bmi<=23 正常範圍)

def calcBmi(h, w):
    bmi = w / (h/100)**2
    print('bmi=%.1f' % bmi)
    if bmi > 23:
        print('過重')
    elif bmi <= 18:
        print('過輕')
    else:
        print('正常')

# Python 主方法
# 若直接執行 DefDemi1.py 則 __name__ 這個 python 內建變數會得到 '__main__'
#print(__name__)
if __name__ == '__main__':
    calcBmi(170, 60)
