# 回傳多筆參數資料

def getTwoSalary():
    return 75000, 25000 # 本薪, 獎金


if __name__ == '__main__':
    x, y = getTwoSalary()
    print(x, y, (x+y))

    x = getTwoSalary()
    print(type(x), x)  # x 會得到一個數組 tuple
    print(x[0], x[1])

