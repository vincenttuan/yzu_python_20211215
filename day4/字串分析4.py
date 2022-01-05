str = '國文=100,數學=90,英文=70'
# 求總分 = ?
subjects = str.split(',')
print(subjects)
國文 = subjects[0]
數學 = subjects[1]
英文 = subjects[2]
print(國文, 數學, 英文)
國文分數 = 國文.split("=")[1]
數學分數 = 數學.split("=")[1]
英文分數 = 英文.split("=")[1]
print(國文分數, 數學分數, 英文分數)
print(國文分數 + 數學分數 + 英文分數)
print(int(國文分數) + int(數學分數) + int(英文分數))