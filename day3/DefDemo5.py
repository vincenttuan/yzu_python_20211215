# 手續費 0.001425
# 交易稅 0.003
# 買進台積電 1 張 每股 616
# 買進: 1 * 1000 * 616 = 616000
# 手續費: 616000 * 0.001425 = 877.8
# CASE 1 手續費不打折
# 手續費折扣後: 877.8 * 1 = 877.8
# 買進成本: 616000 + 877.8 = 616877.8
# CASE 2 手續費打 5 折
# 手續費折扣後: 877.8 * 0.5 = 438.9
# 買進成本: 616000 + 438.9 = 616438.9

# amount = 張數
# price = 股價
# discount = 手續費折扣
fee = 0.001425  # 手續費率
def calcBuyCost(amount, price, discount):
    newfee = fee * discount  # 折扣後手續費率
    buy = amount * 1000 * price  # 買入金額
    cost = buy + (buy * newfee)  # 買入成本 = 買入金額 + 手續費
    print('買入成本: %.1f' % cost)

calcBuyCost(1, 616, 1)
calcBuyCost(1, 616, 0.5)



