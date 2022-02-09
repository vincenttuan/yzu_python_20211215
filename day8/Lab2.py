# 判斷成績是否及格 ?
# 分數介於 0~100, 60以上及格 pass, 反之不及格 fail
def check_score(score):
    if score < 0 or score > 100:
        raise Exception('成績超過(0~100)的指定範圍, 輸入成績：%d' % score)
    print('Pass' if score >= 60 else 'Fail')

def input_score():
    try:
        score = int(input('請輸入成績：'))
        return score
    except ValueError as e:
        raise ValueError('成績輸入錯誤！')

if __name__ == '__main__':
    try:
        score = input_score()
        check_score(score)
    except ValueError as e:
        print('ValueError:', e)
    except Exception as e:
        print('Exception', e)