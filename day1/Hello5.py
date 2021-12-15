# 使用者可以輸入變數內容
x = input("輸入成績:")
print("您所輸入的是:", x, type(x)) # type取得變數的型態
# 字串 str 是無法進行計算與數學比對的
# 要將字串 str 透過 int(x) 變為數字 int
x = int(x)  # 字串轉數字
print("轉換後的結果:", x, type(x)) # type取得變數的型態
if x >= 60:
    print(x, "及格")
else:
    print(x, "不及格")

