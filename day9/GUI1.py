import tkinter
# 建構小視窗
'''
+------------+
|  My Window |
+------------+
|            |
|            |
+------------+
'''
win = tkinter.Tk()  # 取得視窗物件
win.title('My Window')  # 設定視窗抬頭
win.geometry("300x300")  # 設定視窗尺寸大小
win.mainloop()  # GUI 視窗運行
