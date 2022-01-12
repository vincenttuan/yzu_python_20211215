# 2 ~ 10 的質數
# 將結果放到 result 數組中
result = []
for i in range(2, 11):
    for j in range(2, i//2+1):
        #print(i,"%", j, '=', i%j)
        if i%j == 0:
            break # 不執行 else, 進入下一個迴圈
    else: # then 然後的意思
        print(i)
        result.append(i)
print(result)

