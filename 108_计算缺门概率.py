# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 计算52张扑克牌发牌后，一手牌至少缺一门的概率有多大
# 假定牌的编号1~13为黑桃，14~26为红桃，27~39为方块，40~52为梅花

import random
EXP = 100000                                    # 实验次数
DEAL = 13                                       # 发牌张数
void = 0                                        # 缺门计数器
for i in range(EXP):
    S1 = H1 = D1 = C1 = 13                      # 初始时牌堆每门牌13张
    S2 = H2 = D2 = C2 = 0                       # 初始时手牌每门牌0张
    for i in range(DEAL):
        r = random.randint(1,S1+H1+D1+C1)       # 产生一个1到剩余牌张总数的随机数
        if  r <= S1 :                           # 该随机数指定牌张为黑桃
            S1 -= 1                             # 牌堆黑桃张数减1
            S2 = 1                              # 现在手牌里有黑桃了
        elif r <= S1+H1 :                       # 该随机数指定牌张为红桃
            H1 -= 1                             # 牌堆红桃张数减1
            H2 = 1                              # 现在手牌里有红桃了
        elif r <= S1+H1+D1 :                    # 该随机数指定牌张为方块
            D1 -= 1                             # 牌堆方块张数减1
            D2 = 1                              # 现在手牌里有方块了
        else:                                   # 该随机数指定牌张为梅花
            C1 -= 1                             # 牌堆梅花张数减1
            C2 = 1                              # 现在手牌里有梅花了
        full = S2 + H2 + D2 + C2
        if full == 4: break                     # 四门花色都不缺，无需继续发牌
    if full < 4 : void += 1                     # 发完牌，如果有缺门，计数器+1
print ("P(void) = %0.1f" %(void/EXP*100),"%")
