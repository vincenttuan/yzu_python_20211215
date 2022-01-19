# 物件導向
class Person:  # 類別，建構物件的藍圖
    name = ''  # 姓名。物件屬性/變數/欄位/資產
    sex = ''   # 性別
    age = 0    # 年齡，0 是初始值

# python 主程式
if __name__ == '__main__':
    p1 = Person()  # 建立物件
    p2 = Person()  # 建立物件
    p1.name = 'Vincent'  # 設定物件屬性資料
    p1.sex = '男'
    p1.age = 18
    p2.name = 'Anita'
    p2.sex = '女'
    p2.sex = 19
    print(p1, type(p1), p2, type(p2))
    print(p1.name, p1.sex, p1.age)
    print(p2.name, p2.sex, p2.age)
