'''
雞加兔子共有 83 隻,雞的腳加上兔子的腳
共有 240 隻腳,求雞與兔子各有幾隻?

83*2 = 166
240-166=74/2=37 ... 兔子
83-37 ... 雞
'''
total = 83
feet = 240
rabbit = (feet - total*2)/2
chicken = total - rabbit
print('雞: %d 兔: %d' % (chicken, rabbit))