# 自訂例外
class LoginException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "error message: %s" % self.message
    def how2Do(self):
        print('請重新登入')

def login(username, password):
    if(username == 'admin' and password == '1234'):
        return 'pass'
    else:
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