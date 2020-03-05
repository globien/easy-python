# 闪电24点扑克游戏

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

# 定义计算24点的子程序
def find_solution(cards, opers):
    for i in range(24):                     # 数字有24中组合
        for j in range(64):                 # 运算符有64种组合
            exp_list = [cards[i][0], opers[j][0], cards[i][1], opers[j][1], cards[i][2], opers[j][2], cards[i][3] ]               # 交叉拼接数字和符号
            exp = "".join(exp_list)         # 转换为一个字符串
            if abs(eval(exp)-24) < 0.000001 :
                print("Found a solution: ", exp)
                print()
                return 1
            else:
                for k in range(6):
                    exp_list_pare = add_pare(exp_list,k)
                    exp_pare = "".join(exp_list_pare)
                    try: result = eval(exp_pare)    
                    except ZeroDivisionError: continue      
                    if abs(result-24) < 0.000001:
                        print("Found a solution: ", exp_pare)
                        print()
                        return 1
    return 0

# 定义给表达式加括号的子程序
def add_pare(exp_list, n):
    temp_list = list(exp_list)          # 复制列表，避免改变原表
    if n == 0:
        temp_list.insert(0,'(')
        temp_list.insert(4,')')
        return temp_list
    elif n == 1:
        temp_list.insert(2,'(')
        temp_list.insert(6,')')
        return temp_list
    elif n == 2:
        temp_list.insert(4,'(')
        temp_list.append(')')
        return temp_list
    elif n == 3:
        temp_list.insert(0,'(')
        temp_list.insert(6,')')
        return temp_list
    elif n == 4:
        temp_list.insert(2,'(')
        temp_list.append(')')
        return temp_list
    else:
        temp_list.insert(0,'(')
        temp_list.insert(4,')')
        temp_list.insert(6,'(')
        temp_list.append(')')
        return temp_list
    
# 主程序
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
