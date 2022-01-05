str = '170.0,60.0'
#求 bmi
list = str.split(',')
print(list)
h = float(list[0])
w = float(list[1])
print(h, w)
bmi = w / (h/100)**2
print('bmi:', bmi)
