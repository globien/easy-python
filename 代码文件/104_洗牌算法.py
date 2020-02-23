# 一种简单高效的洗牌方法

import random
TOTAL_NUMBER = 54                               # 牌的总张数
DEAL_NUMBER = 54                                # 发牌张数，等于牌的总张数时相当于洗牌
list1 = [i+1 for i in range(TOTAL_NUMBER)]      # 初始化原牌堆，方法无所谓，完整而不重复即可
list2 = []                                      # 新牌堆开始时为空
for i in range(DEAL_NUMBER):
    list2.append(random.choice(list1))          # 从原牌堆中随机抽取一张牌放到新牌堆中
    list1.remove(list2[i])                      # 从原牌堆中删除刚才抽到的那张牌
print("A new card list produced:\n",list2)

# 直接使用Python的shuffle函数洗牌
'''
list1 = [i+1 for i in range(TOTAL_NUMBER)]
random.shuffle(list1)
print("Shuffle directly by random.shuffle function:\n",list1)
'''

# 详述文件: https://github.com/globien/easy_python/blob/master/描述文件/104_如何高效而完美地洗牌.md
