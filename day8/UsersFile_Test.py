lines = open('users.txt', 'r')
users = []
for str in lines.readlines():
    str = str.strip()  # 除去左右空白與斷行符號
    user = dict(item.split("=") for item in str.split(','))
    users.append(user)

print(users)