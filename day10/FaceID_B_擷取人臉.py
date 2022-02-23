# 匯入所需程式庫
import glob
import os
import cv2
from day10 import FaceID_A_參數設定

# 載入 Config.HAAR_FACES 指定的層疊分類器
haar_faces = cv2.CascadeClassifier(FaceID_A_參數設定.HAAR_FACES)

# 主程式
if __name__ == '__main__':
    # 取得攝像鏡頭位置
    camera = cv2.VideoCapture(0)

    # 設定攝像鏡頭捕捉區域
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 假如 config.POSITIVE_DIR 指定的目錄不存在
    if not os.path.exists(FaceID_A_參數設定.POSITIVE_DIR):
        # 新增 config.POSITIVE_DIR 指定的目錄
        os.makedirs(FaceID_A_參數設定.POSITIVE_DIR)

    # 找出 config.POSITIVE_DIR 指定的目錄符合檔案名規則的檔案
    files = sorted(glob.glob(os.path.join(FaceID_A_參數設定.POSITIVE_DIR,
                                          FaceID_A_參數設定.POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
    # 設定計算器為 0
    count = 0

    # 若找到既有的正樣本檔案
    if len(files) > 0:
        # 計算出下個檔案編號
        count = int(files[-1][-7:-4]) + 1

    print('捕獲到正確的訓練圖像')

    # 無窮迴圈
    while count < 201:
        # 捕捉 frame-by-frame (讀取相片)
        ret, image = camera.read()  # ret : 讀到的 frame 是正確的話會回傳 true

        # 將 frame 顯示於視窗中 (這樣才可以看到自己的臉)
        cv2.imshow('Capture', image)

        # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 利用 OpenCV 轉為灰階相片
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # 進行判斷是否是單一人臉的相片
        result = FaceID_A_參數設定.detect_single(gray, haar_faces)

        # 若不是單一人臉的相片
        if result is None:
            # 列印錯誤並請重拍的訊息
            print('無法檢測到單個 opencv_faceid (只可以有一個臉，其他人請讓開)！檢查capture.pgm中的圖像以查看捕獲的內容，並再次嘗試。')
            # 回到迴圈起始位置(重拍)
            continue

        # 取得欲裁切的資料
        x, y, w, h = result

        # 進行裁切
        crop = FaceID_A_參數設定.crop(gray, x, y, w, h)

        # 產生新編檔名
        filename = os.path.join(FaceID_A_參數設定.POSITIVE_DIR, FaceID_A_參數設定.POSITIVE_FILE_PREFIX + '%03d.pgm' % count)

        # 將裁切、縮放、灰階化後得圖片依新編檔名寫入 config.POSITIVE_DIR 指定的目錄
        cv2.imwrite(filename, crop)

        # 列印成功儲存訊息
        print('找到 opencv_faceid 並儲存培訓圖片', filename)

        # 編號加 1
        count += 1

    # 釋放資源
    camera.release()

    # 關閉所有視窗
    cv2.destroyAllWindows()
