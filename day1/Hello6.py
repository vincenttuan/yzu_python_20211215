# 讓使用者輸入半徑 r (可支援小數 = 浮點數), 可以得到圓面積與球體積
r = float(input('輸入半徑:'))
pi = 3.14
area = r * r * pi
volume = 4/3 * pi * r ** 3
print('圓面積:', area)
print('球體積:', volume)
