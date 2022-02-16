import tkinter
# 建構小視窗
'''
+------------+
| My Window2 |
+------------+
|   Label    |
|            |
+-------------
'''
win = tkinter.Tk()  # 取得視窗物件
win.title('My Window 2')  # 設定視窗抬頭
win.geometry("300x300")  # 設定視窗尺寸大小
# 元素配置
label = tkinter.Label(
    win,
    text='Hello',
    bg='yellow',
    font=('Arial, 20'),
    width=30,
    height=5
)
label.pack()

win.mainloop()  # GUI 視窗運行
