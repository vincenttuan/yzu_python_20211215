import math

def my_input():
    r = input('請輸入半徑：')
    try:
        r = float(r)
    except ValueError as e:
        print('輸入錯誤，請重新輸入。錯誤訊息：', e)
        my_input() # 重新調用 my_input()
    else:
        area = math.pi * r ** 2
        print(r, area)

if __name__ == '__main__':
    my_input()