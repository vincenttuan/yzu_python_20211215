str = 'she sell sea shell on the sea shore'
print(len(str))
print(str[2:10])
print('有幾個 s:', str.count('s'))
print('on 的位置:', str.find('on'))
print('off 的位置:', str.find('off'), '(-1表示沒有找到)')
# str 中有沒有 sea 這個字 ?
result = '有' if str.find('sea') >= 0 else '沒有'
print(result, 'sea')
# str 中有沒有 land 這個字 ?
result = '有' if str.find('land') >= 0 else '沒有'
print(result, 'land')
