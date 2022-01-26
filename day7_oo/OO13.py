# 物件的 __get__、__set__
class USD:
    def __get__(self, instance, owner):
        money = instance.money
        return money / 30.5

class JPY:
    def __get__(self, instance, owner):
        money = instance.money
        return money / 0.28

class Exchange:
    usd = USD()
    jpy = JPY()
    def __init__(self, money):
        self.money = money

if __name__ == '__main__':
    twd = 10000
    exchange = Exchange(twd)
    print('TWD:', twd)
    print('USD:', exchange.usd)  # __get__
    print('JPY:', exchange.jpy)  # __get__
