# 0~100之間猜一個數字
import random as r
min = 0
max = 100
ans = r.randint(min+1, max-1)
while(True):
    # 使用者猜
    guess = int(input('使用者 %d ~ %d 之間猜一數字:' % (min, max)))
    if guess < ans:
        min = guess
    elif guess > ans:
        max = guess
    else:
        print('恭喜使用者猜對了')
        break
    # 電腦猜
    pc = r.randint(min+1, max-1)
    print('電腦 %d ~ %d 之間猜一數字:%d' % (min, max, pc))
    if pc < ans:
        min = pc
    elif pc > ans:
        max = pc
    else:
        print('恭喜電腦猜對了')
        break