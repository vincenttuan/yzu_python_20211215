# yzu_python_20211215
元智大學 Python 基礎課程
PPT 連結: 
https://drive.google.com/drive/folders/11TA2-LvvWF-9l4Oo3dEirZoSzCMW3CVT?usp=sharing

<ol>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day1">print 與 input</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day2">資料類型</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day3">方法與模組</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day4">字串應用、條件控制與迴圈控制</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day5">演算法與爬蟲</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day6">檔案存取與爬蟲應用</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day6_oo">物件導向-1</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day7_oo">物件導向-2</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day7_twii">選股策略</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day8">例外處理</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day8_sqlite">SQLite 資料庫</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day9">GUI介面</a></li>
    <li>
        <a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day10">OpenCV 辨識與人臉認識機器學習</a>
    </li>
</ol>

<hr>
<pre>
# 透過經緯度計算距離的方法
def haversine(lon1, lat1, lon2, lat2) -> int: # 經度1，緯度1，經度2，緯度2）
    # 轉弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # 半正矢 haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半徑(公里)
    return c * r * 1000 # 單位公尺
</pre>
<hr>
<pre>
All file modes in Python
r for reading
r+ opens for reading and writing (cannot truncate a file)
w for writing
w+ for writing and reading (can truncate a file)
rb for reading a binary file. The file pointer is placed at the beginning of the file.
rb+ reading or writing a binary file
wb+ writing a binary file
a+ opens for appending
ab+ Opens a file for both appending and reading in binary. The file pointer is at the end of the file if the file exists. The file opens in the append mode.
x open for exclusive creation, failing if the file already exists (Python 3)
</pre>

