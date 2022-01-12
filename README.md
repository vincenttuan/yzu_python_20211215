# yzu_python_20211215
元智大學 Python 基礎課程
PPT 連結: 
https://drive.google.com/drive/folders/11TA2-LvvWF-9l4Oo3dEirZoSzCMW3CVT?usp=sharing
<!--
<ol>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day1">print 與 input</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day2">資料類型</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day3">方法與模組</a></li>
    <li><a href="https://github.com/vincenttuan/yzu_python_20211215/tree/main/day4">字串應用、條件控制與迴圈控制</a></li>
</ol>
-->
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
