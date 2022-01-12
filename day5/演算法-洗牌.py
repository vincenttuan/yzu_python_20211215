# 洗牌-互換位置
import random as r
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9',
         '10', 'J', 'Q', 'K'] * 4
print(poker)
for i in range(100):
    # 洗牌
    x = r.randint(0, len(poker)-1)
    y = r.randint(0, len(poker)-1)
    value = poker[x]
    poker[x] = poker[y]
    poker[y] = value

print(poker)