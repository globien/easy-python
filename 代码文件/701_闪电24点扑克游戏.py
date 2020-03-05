# 闪电24点扑克游戏

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

# 自定义函数，通过组合牌点和运算符，找到一种表达式可以得到24点
def find_solution(cards, opers):
    for i in range(24):                     # 数字有24中组合
        for j in range(64):                 # 运算符有64种组合
            exp_list = [cards[i][0], opers[j][0], cards[i][1], opers[j][1], cards[i][2], opers[j][2], cards[i][3]]   # 交叉拼接数字和符号
            exp = "".join(exp_list)         # 转换为一个字符串
            if abs(eval(exp)-24) < 0.000001:# 判断结果是否为24
                print("Found a solution: ", exp)
                print()
                return 1
            else:                           # 加括号尝试
                for k in range(6):          # 6种加括号的方法
                    exp_list_pare = add_pare(exp_list,k)
                    exp_pare = "".join(exp_list_pare)
                    try: result = eval(exp_pare)    # 处理除零错误
                    except ZeroDivisionError: continue      
                    if abs(result-24) < 0.000001:
                        print("Found a solution: ", exp_pare)
                        print()
                        return 1
    return 0

# 自定义函数，对表达式增加括号，一共有六种有效的加括号方法
def add_pare(exp_list, n):
    temp_list = list(exp_list)          # 复制列表，避免改变原表
    if n == 0:                          # (a ° b) ° c ° d
        temp_list.insert(0,'(')
        temp_list.insert(4,')')
        return temp_list
    elif n == 1:                        # a ° (b ° c) ° d
        temp_list.insert(2,'(')
        temp_list.insert(6,')')
        return temp_list
    elif n == 2:                        # a ° b ° (c ° d)
        temp_list.insert(4,'(')
        temp_list.append(')')
        return temp_list
    elif n == 3:                        # (a ° b ° c) ° d
        temp_list.insert(0,'(')
        temp_list.insert(6,')')
        return temp_list
    elif n == 4:                        # a ° (b ° c ° )
        temp_list.insert(2,'(')
        temp_list.append(')')
        return temp_list
    else:                               # (a ° b) ° (c ° d)
        temp_list.insert(0,'(')
        temp_list.insert(4,')')
        temp_list.insert(6,'(')
        temp_list.append(')')
        return temp_list
    
# 主程序，循环运行直到用户要求退出
all = [i for i in range(1,11) for j in range(16 if i==1 else 4)]
while True:                                 # 无线循环
    shuffle(all)                            # 洗牌
    four = [str(all[i]) for i in range(4)]  # 发四张牌
    # cards_four = ["8", "8", "3", "3"]     # 指定4张牌用于测试
    print("四张牌是：", four)
    input("请思考并计算，按回车键看小蟒的答案...")
    cards = list(permutations(four,4))      # 4张牌全部排列组合
    opers = list(product(["+","-","*","/"], repeat=3))
    if find_solution(cards, opers) == 0:
        print("There is no solution.\n")
    cmd = input("按回车键继续游戏（或‘q’退出）...")
    if cmd.lower() == 'q': 
        print("游戏已结束。")
        break
