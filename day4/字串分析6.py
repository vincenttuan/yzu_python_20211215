str = '小明本薪$65000,今年公司發放6個月,試問小明年終'

salary = int(str[str.find('$')+1:str.find(',')])
print('salary:', salary)
month = int(str[ str.find('發放')+2 : str.find('個月')])
print('month:', month)
print(salary * month)
