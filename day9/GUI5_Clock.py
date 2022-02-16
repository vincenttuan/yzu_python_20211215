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

def win_exit():
    win.quit()

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('My Clock')
    var = tkinter.StringVar()
    time_label = tkinter.Label(win, textvariable=var, fg='blue', font=('Arial', 80))
    time_label.pack()
    exit_button = tkinter.Button(win, text="Exit", font=('Arial', 30), command=win_exit)
    exit_button.pack()
    gettime()
    win.mainloop()


