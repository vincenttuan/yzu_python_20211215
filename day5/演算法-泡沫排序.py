# 泡沫排序法: Bubble Sort
'''
7 5 6 1 (原始)
--------------
5 7 6 1
5 6 7 1
5 6 1 7
--------------
5 6 1 7
5 1 6 7
--------------
1 5 6 7
'''
data = [7, 5, 6, 1]
n = len(data)
for i in range(n-1):
    for j in range(n-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j] # 資料互換

print(data)
