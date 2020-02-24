# 分别通过理论计算和随机实验来验证一个班上有相同生日的概率问题
# 理论公式：Pn = 1 - 365!/(365^n * (365-n)!)

import random
import math

n = int(input("请输入一个班有多少人："))

# 按相关公式计算理论值
Pn = 1 - math.factorial(365) / (365**n * math.factorial(365-n))
print("一个班", n, "个人中至少有两个人生日相同的概率:")
print("理论值 =", Pn)

# 进行随机实验
EXP_NUM = 10000             # 实验次数
counter = 0                 # 计数器，统计出现重复生日的次数
birthdays = []              # 用来存储随机产生的生日的列表
for i in range(EXP_NUM):
    for j in range(n):
        birthdays.append(random.randint(1,365)) # 产生生日表
    if len(birthdays) > len(set(birthdays)):    # 如果有重复
        counter = counter + 1                   # 累计重复次数
    birthdays = []                              # 重置生日表
print("实验值 =", counter/EXP_NUM)


# 详述文件：https://github.com/globien/easy_python/blob/master/描述文件/107_生日相同的概率问题.md
