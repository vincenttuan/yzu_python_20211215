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
keyword = input('請輸入關鍵字: ')
for food in bad_foods:
    if keyword in food['品名']:
        print(food)

