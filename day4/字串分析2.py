str = '   she sell sea shell on the sea shore   '
print(len(str))
# 去除左右空白 strip()
# 只去除左空白 lstrip()
# 只去除右空白 rstrip()
str = str.strip()
print(len(str))
# 'she sell sea shell on the sea shore'
words = str.split() # 利用空白切割字串
print(type(words), words)
print('第一個字:', words[0], type(words[0]))
print('總共有多少字:', len(words))
print('最後一個字:', words[-1])