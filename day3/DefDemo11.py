# 雞加兔子共有 83 隻,雞的腳加上兔子的腳
# 共有 240 隻腳,求雞與兔子各有幾隻?
# 寫一個 def getRabbitAndChicken 方法
# 此方法會回傳 rabbit, chicken 的數量
def getRabbitAndChicken(sum, feet):
    if feet/4 <= sum <= feet/2 and feet % 2 == 0:
        rabbit = (feet - sum * 2) / 2
        chicken = sum - rabbit
    else:
        print('無法計算')
        return 0, 0  # 提早回傳
    return rabbit, chicken # 正常回傳

if __name__ == '__main__':
    r, c = getRabbitAndChicken(83, 240)
    print('兔子: %d 雞: %d' % (r, c))
    r, c = getRabbitAndChicken(30, 240)
    print('兔子: %d 雞: %d' % (r, c))