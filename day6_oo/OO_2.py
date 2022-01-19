# 物件導向
class Person:  # 類別，建構物件的藍圖
    name = ''  # 姓名。物件屬性/變數/欄位/資產
    sex = ''   # 性別
    age = 0    # 年齡，0 是初始值

    def __str__(self) -> str:
        return "name=%s sex=%s age=%d" % (self.name, self.sex, self.age)


# python 主程式
if __name__ == '__main__':
    p1 = Person()  # 建立物件
    p1.name = 'Vincent'  # 設定物件屬性資料
    p1.sex = '男'
    p1.age = 18
    print(p1)
