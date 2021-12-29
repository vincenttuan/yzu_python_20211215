import random as r
# 幸運數字
def getLuckyNumber():
    num = r.randint(1, 100)
    return num

# 主方法
if __name__ == '__main__':
    # n 就可以接到 getLuckyNumber() return 的結果
    n = getLuckyNumber()
    print(n)
    print(getLuckyNumber())