import json
import requests
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
data = json.loads(requests.get(url).text)
print(data)

# 資料整理
print('資料整理:')
bad_foods = []
for d in data:
    food = {'品名': d.get('品名'), '不合格原因': d.get('不合格原因')}
    bad_foods.append(food)
print(bad_foods)

# 資料分析
print('資料分析:')
target_foods = []
keyword = input('請輸入關鍵字: ')
for food in bad_foods:
    if keyword in food['品名']:
        print(food)
        target_foods.append(food)

# Lab 資料寫入
# 請將透過關鍵字「池上」所搜尋到的結果，逐筆寫入到 bad_foods.txt
# 寫完 +10
# 提示：r: read, w: write(清除原有資料並寫入), a: append(保留原有資料並寫入)
file = open('bad_foods.txt', 'w', encoding='UTF-8')
for target in target_foods:
    file.write(str(target))
    file.write('\n')

print('寫檔成功')