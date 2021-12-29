# 手續費率 0.001425
# 交易稅率 0.003
# 賣出台積電 1 張 每股 616
# 賣出 = 1 * 1000 * 616 = 616000
# 手續費 = 616000 * 0.001425 = 877.8
# 交易稅 = 616000 * 0.003 = 1848
# 金額 = 616000 - 877.8 - 1848 = 613274.2

fee = 0.001425  # 手續費率
tax = 0.003 # 交易稅率
def calcSell(amount, price, discount):
    newfee = fee * discount
    sell = amount * 1000 * price
    total = sell - (sell*newfee) - (sell*tax)
    print('Total: %.1f' % total)

# Python 主方法
if __name__ == '__main__':
    calcSell(1, 616, 1)
    calcSell(1, 616, 0.5)
