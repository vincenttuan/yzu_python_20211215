# 物件與運算子
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        self.n = self.n + x

    def __sub__(self, x):
        self.n = self.n - x

    def __pow__(self, power, modulo=None):
        self.n = self.n ** power

    def __str__(self):
        return str(self.n)

if __name__ == '__main__':
    x = Number(10)
    x + 15  # 配 __add__
    x - 3   # 配 __sub__
    x ** 2  # 配 __pow__
    print(x)
