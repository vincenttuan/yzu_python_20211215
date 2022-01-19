file = open('salary.txt', 'r', encoding='UTF-8')  # encoding='BIG5'
content = file.read()
print(type(content), content)

file = open('salary.txt', 'r', encoding='UTF-8')
lines = file.readlines()
print(type(lines), lines)

# 去除 \n
print(lines[0].strip('\n'))


