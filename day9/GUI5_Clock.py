import tkinter
import time

'''
+------------+
|  My Clock  |
+------------+
|  19:28:32  |
|    EXIT    |
+------------+
'''
def gettime():
    var.set(time.strftime("%H:%M:%S"))  # 得到當下的時間
    win.after(1000, gettime)  # 每隔一秒鐘(1000ms)再度呼叫 gettime 方法

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('My Clock')
    var = tkinter.StringVar()
    time_label = tkinter.Label(win, textvariable=var, fg='blue', font=('Arial', 80))
    time_label.pack()
    gettime()
    win.mainloop()


