# 闪电24点扑克游戏
# 暴力测试 24 x 64 x 6 = 9216 种排列组合（包括大量等效重复的）
# 随机发牌，找到一个解即算成功。重复游戏直到用户指示退出。

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

# 自定义函数，通过组合牌点和运算符，找到一种表达式可以得到24点
def find_solution(cards, opers):
    for i in range(24):                     # 数字有24中组合
        for j in range(64):                 # 运算符有64种组合
            seq = [cards[i][0], ops[j][0], cards[i][1], ops[j][1], cards[i][2], ops[j][2], cards[i][3]]   # 交叉拼接数字和符号形成序列
            exp = "".join(seq)              # 序列转换为字符串
            if abs(eval(exp)-24) < 0.000001:# 判断结果是否为24
                print("Found a solution: ", exp)
                print()
                return 1
            else:                           # 加括号尝试
                for k in range(6):          # 6种加括号的方法
                    seq_pare = add_pare(seq,k)   # 调加括号函数
                    exp_pare = "".join(seq_pare) # 序列转换为串
                    try: 
                        result = eval(exp_pare)  # 处理除零错误
                    except ZeroDivisionError: continue      
                    if abs(result-24) < 0.000001:
                        print("Found a solution: ", exp_pare)
                        print()
                        return 1
    return 0

# 自定义函数，对表达式增加括号，一共有六种有效的加括号方法
def add_pare(sequence, n):
    temp = list(sequence)          # 复制列表，并避免改变原表
    if n == 0:                     # (a ° b) ° c ° d
        temp.insert(0,'(')
        temp.insert(4,')')
        return temp
    elif n == 1:                   # a ° (b ° c) ° d
        temp.insert(2,'(')
        temp.insert(6,')')
        return temp
    elif n == 2:                   # a ° b ° (c ° d)
        temp.insert(4,'(')
        temp.append(')')
        return temp
    elif n == 3:                   # (a ° b ° c) ° d
        temp.insert(0,'(')
        temp.insert(6,')')
        return temp
    elif n == 4:                   # a ° (b ° c ° )
        temp.insert(2,'(')
        temp.append(')')
        return temp
    else:                          # (a ° b) ° (c ° d)
        temp.insert(0,'(')
        temp.insert(4,')')
        temp.insert(6,'(')
        temp.append(')')
        return temp
    
# 主程序，循环运行直到用户要求退出
all = [i for i in range(1,11) for j in range(16 if i==1 else 4)]
while True:                                 # 无线循环
    shuffle(all)                            # 洗牌
    deal = [str(all[i]) for i in range(4)]  # 发四张牌
    # deal = ["6", "5", "1", "4"]           # 指定4张牌用于测试
    print("四张牌是：", deal)
    input("请思考并计算，按回车键看小蟒的答案...")
    cards = list(permutations(deal,4))      # 4张牌全部排列组合
    ops = list(product(["+","-","*","/"], repeat=3))    # 四种运算符取3个的全部排列组合
    if find_solution(cards, ops) == 0:      # 调用自定义函数暴力求解
        print("There is no solution.\n")    # 所有排列组合都不成功
    cmd = input("按回车键继续游戏（或‘q’退出）...")
    if cmd.lower() == 'q': 
        print("游戏已结束。")
        break
