#計算圓面積的 def
def calcArea(r) :
    area = r * r * 3.14
    print('半徑=%d 圓面積=%.1f' % (r, area))

#計算球體積的 def
def calcVolume(r):
    volume = 4/3 * 3.14 * r ** 3
    print('半徑=%d 球體積=%.1f' % (r, volume))

# Python 主方法
if __name__ == '__main__':
    calcArea(13)
    calcArea(15)
    calcVolume(13)
    calcVolume(15)

