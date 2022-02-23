import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)  # 320, 640, 800, 1024
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)  # 240, 480, 600, 768

# 人臉特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()  # 捕捉影像資料
    print(ret, frame)

    # 顯示影像
    cv2.imshow('My Window', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 將視窗全部清除
cap.release()
cv2.destroyAllWindows()
