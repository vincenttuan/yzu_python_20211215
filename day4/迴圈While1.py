# while 迴圈
import random as r
while(True):
    n = r.randint(1, 99)  # 1~99 之間取隨機數
    print(n)
    if n == 99:
        break  # 跳離迴圈
