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

win = tkinter.Tk()
win.title('BMI 計算機')
win.geometry("600x250")
# 建立元件
myfont = font.Font(family='Arial', size=36, weight='bold')
h_label = tkinter.Label(text='身高', font=myfont)
h_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
w_label = tkinter.Label(text='體重', font=myfont)
w_entry = tkinter.Entry(font=myfont, justify=tkinter.RIGHT)
rest_btn = tkinter.Button(text='清除', font=myfont)
submit_btn = tkinter.Button(text='計算', font=myfont)
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
result_label.grid(row=1, column=1, sticky='EWNS', columnspan=1)

win.mainloop()