# 闪电24点扑克游戏

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

# 定义给表达式加括号的子程序
def add_括号(exp_list, n):
    temp_list = list(exp_list)              # 复制列表
    if n >= 0:
        temp_list.insert(0,'(')
        temp_list.insert(4,')')
        return temp_list
    

# 定义计算24点的子程序
def find_solution(cards, signs):
    for i in range(24):
        for j in range(24):
            exp = cards[i][0]+signs[j][0]+cards[i][1]+signs[j][1]+cards[i][2]+signs[j][2]+cards[i][3]
            if abs(eval(exp)-24) < 0.000001 :
                print("Find a solution: ", exp)
                return
            else:
                exp_list = list(exp)
                for i in range(7):
                    list_括号 = add_括号(exp_list,i)
                    exp_括号 = "".join(list_括号)
                    print(exp_括号)
                    if abs(eval(exp_括号)-24) < 0.000001:
                        print("Find a solution: ", exp_括号)
                        return

cards_all = [i for i in range(1,11) for j in range(16 if i==1 else 4)]
shuffle(cards_all)                                  # 洗牌
cards_four = [str(cards_all[i]) for i in range(4)]  # 发四张牌
# cards_four = ["3", "8", "1", "1"]
print(cards_four)
cards = list(permutations(cards_four,4))
signs = list(permutations(["+","-","*","/"],3))

find_solution(cards, signs)
