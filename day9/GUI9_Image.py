import tkinter
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO
# 先要安裝 pillpow
win = tkinter.Tk()
url = 'http://cdn.unwire.hk/wp-content/uploads/2020/12/maxresdefault-1.jpg'

raw_data = urllib.request.urlopen(url).read()  # byte[]
im = Image.open(BytesIO(raw_data))  # 轉 Image
photo = ImageTk.PhotoImage(im)  # 轉 PhotoImage

car_label = tkinter.Label(image=photo)
#car_label.image = photo
car_label.pack()

win.mainloop()