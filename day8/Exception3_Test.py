# 巢狀例外
# 讀寫一個檔案
# 1. 開啟檔案, 2. 寫入檔案
try:
    f = open('demo.txt', 'r')
    try:
        f.write('Happy New Year 2022')
    except:
        print('寫入資料失敗')
    finally:
        print('關閉檔案')
        f.close()
except:
    print('開啟檔案失敗')
