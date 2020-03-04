# 闪电24点扑克游戏

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

# 定义计算24点的子程序
def find_solution(cards, signs):
    for i in range(24):
        for j in range(24):
            exp_list = [cards[i][0], signs[j][0], cards[i][1], signs[j][1], cards[i][2], signs[j][2], cards[i][3] ]
            exp = "".join(exp_list)       # 把列表合并为字符串
            print(i, j, exp)
            if abs(eval(exp)-24) < 0.000001 :
                print("Found a solution: ", exp)
                return 1
            else:
                # exp_list = ["8","/","3","-","8","/","3"]
                for k in range(6):
                    exp_list_pare = add_pare(exp_list,k)
                    exp_pare = "".join(exp_list_pare)
                    # print(exp_pare)
                    try: result = eval(exp_pare)    
                    except ZeroDivisionError: continue      
                    if abs(result-24) < 0.000001:
                        print("Found a solution: ", exp_pare)
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
cards_all = [i for i in range(1,11) for j in range(16 if i==1 else 4)]
shuffle(cards_all)                                  # 洗牌
cards_four = [str(cards_all[i]) for i in range(4)]  # 发四张牌
cards_four = ["8", "8", "3", "3"]
print(cards_four)
cards = list(permutations(cards_four,4))
signs = list(permutations(["+","-","*","/"],3))

if find_solution(cards, signs) == 0:
    print("There is no solution.")
