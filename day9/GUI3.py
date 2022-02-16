import tkinter
# 建構小視窗
'''
+------------+
| My Window2 |
+------------+
|   Label    |
| BTN1 BTN2  |
+-------------
'''
win = tkinter.Tk()  # 取得視窗物件
win.title('My Window 2')  # 設定視窗抬頭
win.geometry("300x300")  # 設定視窗尺寸大小
# Label 元素配置
label = tkinter.Label(
    win,
    text='Hello',
    bg='yellow',
    font=('Arial, 20'),
    width=30,
    height=5
)
label.pack()
# Button 元素配置
button1 = tkinter.Button(win, text="OK", width=10, height=2, font=('Arial', 20))
button2 = tkinter.Button(win, text="Exit", width=10, height=2, font=('Arial', 20))
button1.pack(side=tkinter.LEFT)
button2.pack(side=tkinter.RIGHT)
win.mainloop()  # GUI 視窗運行
