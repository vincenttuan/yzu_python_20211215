import math
# 求二點之間的距離
x1, y1 = 10, 20
x2, y2 = 15, 45

x = math.pow(x1-x2, 2)
y = math.pow(y1-y2, 2)
d = math.sqrt(x + y)
print(d)
