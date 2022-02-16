import tkinter
from tkinter import messagebox
# 建構小視窗

'''
+------------+
| My Window4 |
+------------+
|     5      |
| Add   Exit |
+-------------
'''
value = 0

def add():
    global value
    value += 1
    var.set(str(value))

def win_exit():
    win.quit()

if __name__ == '__main__':
    win = tkinter.Tk()  # 取得視窗物件
    win.title('My Window 4')  # 設定視窗抬頭
    win.geometry("300x300")  # 設定視窗尺寸大小
    # Label 元素配置
    var = tkinter.StringVar()  # 字串參照物件
    var.set("0")
    label = tkinter.Label(
        win,
        textvariable=var,
        bg='yellow',
        font=('Arial, 20'),
        width=30,
        height=5
    )
    label.pack()
    # Button 元素配置
    button1 = tkinter.Button(win, text="Add", width=10, height=2, font=('Arial', 20), command=add)
    button2 = tkinter.Button(win, text="Exit", width=10, height=2, font=('Arial', 20), command=win_exit)
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.RIGHT)
    win.mainloop()  # GUI 視窗運行
