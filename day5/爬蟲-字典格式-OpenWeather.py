import requests
import ssl
import json
import datetime
# 不用驗證 SSL
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s,tw&appid=%s'
city_name = 'taoyuan'
code = 'fcc57465b76d35357c84e4e30fe2431a'
url = url % (city_name, code)
print(url)
resp = requests.get(url)
print(resp.status_code)
if resp.status_code != 200:
    print('資料取得失敗')
    exit(0)

# 將網頁的字串內容轉換成可處理的 json 物件(jo)
jo = json.loads(resp.text)
print(jo)
name = jo['name']
print('地區=', name)
dt = jo['dt']
dt = datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
print('時間=', dt)
main = jo['weather'][0]['main']
description = jo['weather'][0]['description']
print('天氣說明:', main, description)
temp = jo['main']['temp'] - 273.15
print('氣溫: %.2f°C' % temp)
feels_like = jo['main']['feels_like'] - 273.15
print('體感溫度: %.2f°C' % feels_like)
humidity = jo['main']['humidity']
print('濕度: %d%%' % humidity)