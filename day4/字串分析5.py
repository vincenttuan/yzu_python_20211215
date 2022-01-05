str = '客戶:小明 股號:2330 股數:5100 買進價:616'
# 請算出小明買進成本(不含手續費)
# 不使用 split()
a = str[str.find('股數'):str.find('買進價')]
print('a =', a)
amount = a[a.find(':')+1:]
amount = amount.strip()
amount = int(amount)
print(type(amount), amount)
b = str[str.find('買進價:'):]
print('b = ', b)
price = float(b[b.find(':')+1:].strip())
print(type(price), price)
print(amount * price)