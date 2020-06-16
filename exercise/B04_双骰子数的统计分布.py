import random
import numpy as np                          # 非常有用的数学库函数模块，尤其是数组、矩阵等
import matplotlib.pyplot as plt             # 非常有用数学、科学作图模块

trial = 100000
dice = (1, 2, 3, 4, 5, 6)

stats = {}                                  # 定义一个字典，用来存放每个数字及它出现的次数
for i in range(trial):
    two_dice = random.choice(dice) + random.choice(dice)    # 得到两个骰子的组合数
    if two_dice not in stats:
        stats[two_dice] = 1                 # 该组合数在字典中还没有，说明这是它第一次出现
    else:
        stats[two_dice] += 1                # 该组合数在字典中已有了，其计数累加1

stats = dict(sorted(stats.items()))         # 对结果按组合数数字排序（并还原为字典结构）
print(stats)
x = list(stats.keys())                      # 把组合数作为横坐标
y = np.array(list(stats.values()))/trial    # 把累计出现次数的比例作为纵坐标
plt.bar(x, y)                               # 作图（直方图）
plt.show()                                  # 显示图形
