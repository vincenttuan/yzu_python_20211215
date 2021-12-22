# print
symbol = '2330'  # 股票代號
name = '台積電'  # 股票名稱
price = 610.5  # 價格
amount = 3000  # 買進股數
total = price * amount
# 股票代號:2330 股票名稱:台積電 價格:$610.5 買進股數:3000 投資金額:$xxx
print("股票代號:%s 股票名稱:%s 價格:$%.1f 買進股數:%d 投資金額:$%d" % (symbol, name, price, amount, total))

print('投資金額:$%d' % total) # 1831500
print('投資金額:$%s' % format(total, ',')) # 1,831,500.0
print(type(total))
print('投資金額:$%s' % format(int(total), ',')) # 1,831,500

# 原 : area = 12345.6789
# 改 : area = 12,345.6  # 有千分號 + 小數點一位
area = 12345.6789
print('area*10 : ', area*10)
print('int(area*10) : ', int(area*10))
print('int(area*10)/10 : ', int(area*10)/10)
print('area = %s' % format(int(area*10)/10, ','))
print('area = %s' % format(int(area*100)/100, ','))
print('area = %s' % format(int(area*1000)/1000, ','))
dot = 2
print('area = %s' % format(int(area*10**dot)/(10**dot), ','))