'''
BMI 計算機
+--------+---------+
| Height |  170.0  |  <-- Label, Entry
+--------+---------+
| Weight |   60.5  |  <-- Label, Entry
+--------+---------+
|  Reset |  Submit |  <-- Button, Button
+--------+---------+
|   BMI  |  20.76  |  <-- Label, Label
+--------+---------+
'''
import tkinter
from tkinter import font

def calc():
    h = float(h_entry.get())
    w = float(w_entry.get())
    bmi = w / (h/100) ** 2
    result_label.configure(text="%.2f" % bmi)

def clean():
    # 清除欄位資料
    h_entry.delete(0, tkinter.END)
    w_entry.delete(0, tkinter.END)
    # 還原預設值
    h_entry.insert(0, '0')
    w_entry.insert(0, '0')
    result_label.configure(text="0.00")

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('BMI 計算機')
    win.geometry("600x250")
    # 建立元件
    myfont = font.Font(family='Arial', size=36, weight='bold')
    h_label = tkinter.Label(text='身高', font=myfont)
    h_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
    w_label = tkinter.Label(text='體重', font=myfont)
    w_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
    rest_btn = tkinter.Button(text='清除', font=myfont, command=clean)
    submit_btn = tkinter.Button(text='計算', font=myfont, command=calc)
    bmi_label = tkinter.Label(text='BMI', font=myfont)
    result_label = tkinter.Label(text='0.00', font=myfont)
    # 元件內容初始值
    h_entry.insert(0, 0)
    w_entry.insert(0, 0)
    # 欄列同步 size
    win.columnconfigure((0, 1), weight=1)
    win.rowconfigure((0, 1, 2, 3), weight=1)
    # Grid 佈局
    h_label.grid(row=0, column=0, sticky='EWNS', columnspan=1)
    h_entry.grid(row=0, column=1, sticky='EWNS', columnspan=1)
    w_label.grid(row=1, column=0, sticky='EWNS', columnspan=1)
    w_entry.grid(row=1, column=1, sticky='EWNS', columnspan=1)
    rest_btn.grid(row=2, column=0, sticky='EWNS', columnspan=1)
    submit_btn.grid(row=2, column=1, sticky='EWNS', columnspan=1)
    bmi_label.grid(row=3, column=0, sticky='EWNS', columnspan=1)
    result_label.grid(row=3, column=1, sticky='EWNS', columnspan=1)

    win.mainloop()
