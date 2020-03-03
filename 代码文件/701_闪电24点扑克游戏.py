# 闪电24点扑克游戏

from random import *                        # 导入随机函数
from itertools import *                     # 导入概率统计函数

cards_all = [i for i in range(1,11) for j in range(16 if i==1 else 4)]


shuffle(cards_all)                                  # 洗牌
cards_four = [str(cards_all[i]) for i in range(4)]  # 发四张牌
print(cards_four)
cards = list(permutations(cards_four,4))
signs = list(permutations(["+","-","*","/"],3))

for j in range(5):
    exp = cards[0][0]+signs[j][0]+cards[0][1]+signs[j][1]+cards[0][2]+signs[j][2]+cards[0][3]
    print(eval(exp))



