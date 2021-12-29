import random as r

n = r.randint(1, 100)
if n % 2 == 0:
    print(n, '是偶數')
else:
    print(n, '是奇數')

print(n, '是偶數' if n % 2 == 0 else '是奇數')
