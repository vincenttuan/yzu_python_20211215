# 物件的比較
# >、<、== ...
class Drink:
    def __init__(self, name, amount, total_price):
        self.name = name
        self.amount = amount
        self.price = total_price

    def __lt__(self, other):
        return (self.price/self.amount) < (other.price/other.amount)

    def __gt__(self, other):
        return (self.price/self.amount) > (other.price/other.amount)

if __name__ == '__main__':
    milk = Drink('牛奶', 3, 80)
    coffee = Drink('咖啡', 2, 110)
    print(milk < coffee)
    name = milk.name if milk < coffee else coffee.name
    print('便宜的是: %s' % (name))
    name = milk.name if milk > coffee else coffee.name
    print('較貴的是: %s' % (name))