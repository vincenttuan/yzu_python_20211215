# 參考 Lab3 寫一個登入程式
# 資料比對來源：users.txt
from day8.Lab3 import LoginException

def getUsers():
    lines = open('users.txt', 'r')
    users = []
    for str in lines.readlines():
        str = str.strip()  # 除去左右空白與斷行符號
        user = dict(item.split("=") for item in str.split(','))
        users.append(user)
    return users

def login(username, password):
    users = getUsers()
    for user in users:
        if(user.get('username') == username and user.get('password') == password):
            return True

    raise LoginException('登入失敗')

if __name__ == '__main__':
    username = input('請輸入 username: ')
    password = input('請輸入 password: ')
    try:
        check = login(username, password)
    except LoginException as e:
        print(e)
        e.how2Do()
    else:
        print(check)