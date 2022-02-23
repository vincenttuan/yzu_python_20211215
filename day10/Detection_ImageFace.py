import cv2

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

# 讀檔
frame = cv2.imread('./image/test.jpg')

# 將彩色圖片(RGB)進行灰階(Gray)處理
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# 偵測臉部，得到臉部區域座標與長寬(x, y, w, h)
faces = face_cascade.detectMultiScale(
    gray, # 待檢測圖片
    scaleFactor=1.1, # 檢測粒度(數字越小越精準(速度慢), 反之數字越大越模糊(速度快))
    minNeighbors=5, # 檢測次數(每個目標至少要檢測通過幾次才算成功，才被認定是 face)
    minSize=(30, 30), # 搜尋比對最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE # 比對物類型
)
print("臉部座標(x,y,w,h)", faces)

# 在 face 周圍畫上矩形
for (x, y, w, h) in faces:
    # 參數：frame, 坐上角座標, 右下角座標, BGR 色碼, 框線的寬度
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 將 frame 顯示
cv2.imshow('My window', frame)

# 按下任意鍵離開程式
c = cv2.waitKey(0)
print(c)
