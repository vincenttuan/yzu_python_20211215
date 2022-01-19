# 物件導向
class Person:  # 類別，建構物件的藍圖
    name = ''  # 姓名。物件屬性/變數/欄位/資產
    __sex = ''   # 性別 (有加 __ 的是私有變數沒加的是公有變數)
    age = 0    # 年齡，0 是初始值

    def __init__(self, name, sex, age) -> None:
        self.name = name
        self.__sex = sex
        self.age = age

    def __str__(self) -> str:
        return "name=%s sex=%s age=%d" % (self.name, self.__sex, self.age)


# python 主程式
if __name__ == '__main__':
    p1 = Person('Vincent', '男', 18)  # 建立物件
    p1.__sex = '女'  # 外界無法改動私有變數的內容
    print(p1)
