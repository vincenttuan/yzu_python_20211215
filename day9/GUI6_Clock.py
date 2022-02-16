import threading
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
def playtime():
    while True:
        gettime()
        time.sleep(1)

def gettime():
    strtime = time.strftime("%H:%M:%S")  # 得到當下的時間
    time_label.configure(text=strtime)  # 直接修改 label 文字內容

def win_exit():
    win.quit()

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('My Clock')
    time_label = tkinter.Label(win, text='', fg='blue', font=('Arial', 80))
    time_label.pack()
    exit_button = tkinter.Button(win, text="Exit", font=('Arial', 30), command=win_exit)
    exit_button.pack()
    # 建立執行緒
    t1 = threading.Thread(target=playtime)
    t1.setDaemon(1)  # 設定成背景執行緒
    t1.start()  # 啟動執行緒

    win.mainloop()


