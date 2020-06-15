# 输入分数，打印等级。需要对输入进行错误控制。
while True:
    try:
        score = eval(input("Please input the score: "))
    except:
        print('Illegal input! Try again.')
    else:
        if 0 <= score <= 100:
            break
        else:
            print('Not in the range of 0~100. Try again.')

level = ['不及格', '及格', '中等', '良好', '优秀']
print(level[min(4, max(0, (score-60)//10+1))])  # 分数-等级转换，可以用if-elif-else结构代替
