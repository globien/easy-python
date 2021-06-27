# -*-coding:utf-8 -*-

"""
# File       : 101_24点的另一种算法.py
# Time       ：2021-03-26 2:40 下午
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""
from itertools import permutations, product
def game24(n1,n2,n3,n4):
        for a,b,c,d in permutations((n1,n2,n3,n4),4):
            for o1,o2,o3 in product(['+','-','*','/'], repeat=3): # 笛卡尔积的另一种写法
                cases = list()
                cases.append('%d%s%d%s%d%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('(%d%s%d)%s%d%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('%d%s%d%s(%d%s%d)'%(a,o1,b,o2,c,o3,d))
                cases.append('%d%s(%d%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('(%d%s%d)%s(%d%s%d)'%(a,o1,b,o2,c,o3,d))
                cases.append('(%d%s%d%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('((%d%s%d)%s%d)%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('(%d%s(%d%s%d))%s%d'%(a,o1,b,o2,c,o3,d))
                cases.append('%d%s(%d%s%d%s%d)'%(a,o1,b,o2,c,o3,d))
                cases.append('%d%s((%d%s%d)%s%d)'%(a,o1,b,o2,c,o3,d))
                cases.append('%d%s(%d%s(%d%s%d))'%(a,o1,b,o2,c,o3,d))
                for expression in cases:
                    try: # 捕获表达式中分母为0的异常
                        if eval(expression) == 24:
                            print('答案：%s = 24'%expression)
                            return
                    except:
                        pass
        print('无解！')


game24(5, 5, 5, 1)
game24(1, 3, 4, 6)
game24(10, 10, 4, 4)
game24(7, 7, 3, 3)
game24(1, 5, 7, 10)
game24(15, 25, 37, 80)