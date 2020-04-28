# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

import random
import matplotlib.pyplot as plt

def 成绩统计(成绩表):
    统计表 = {}                      # 以字典方式，生成一张空的统计表
    for 分数 in 成绩表:
        if 分数 in 统计表:
            统计表[分数] += 1        # 如果某个分数已经出现过了，这里累加1
        else:
            统计表[分数] = 1         # 该分数在"成绩表"里，但不在"统计表"里，说明是第一次出现
    return 统计表

# 按正态分布生成一个假设的成绩表，但避免低于0分和高于100分的情况，然后排序
某次成绩表 = [min(100, max(0, int(random.normalvariate(65, 12)))) for i in range(1000)]
某次成绩表.sort()

成绩统计表 = 成绩统计(某次成绩表)
print(成绩统计表)

plt.bar(成绩统计表.keys(), 成绩统计表.values())
plt.show()
