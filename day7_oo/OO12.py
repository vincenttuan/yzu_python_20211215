# 物件的 __get__、__set__
class Celsius: # 攝氏
    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9
    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5

class Temperature: # 溫度
    celsius = Celsius()  # 組合（內部類別）
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

if __name__ == '__main__':
    temp = Temperature(212)
    print('華氏：', temp.fahrenheit, '攝氏：', temp.celsius)  # 呼叫 __get__
    t = 0
    temp.celsius = t  # 呼叫 __set__
    print('攝氏：', t, '華氏：', temp.fahrenheit)