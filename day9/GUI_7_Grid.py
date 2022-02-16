import tkinter
from tkinter import font
'''
+------+-------------+
| btn1 |    btn2     |
+------+------+------+
| btn3 | btn3 | btn4 |
+-------------+------+
'''
win = tkinter.Tk()
myfont = font.Font(family='Arial', size=100, weight='bold')
btn1 = tkinter.Button(text='btn1', font=myfont)
btn2 = tkinter.Button(text='btn2', font=myfont)
btn3 = tkinter.Button(text='btn3', font=myfont)
btn4 = tkinter.Button(text='btn4', font=myfont)
btn5 = tkinter.Button(text='btn5', font=myfont)
# 欄同步 size
win.columnconfigure((0, 1, 2), weight=1)
# 列同步 size
win.rowconfigure((0, 1), weight=1)

btn1.grid(row=0, column=0, sticky='EWNS')
btn2.grid(row=0, column=1, columnspan=2, sticky='EWNS')  # 無縫隙元件填滿
btn3.grid(row=1, column=0, sticky='EWNS')
btn4.grid(row=1, column=1, sticky='EWNS')
btn5.grid(row=1, column=2, sticky='EWNS')

win.mainloop()