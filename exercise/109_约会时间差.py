# -*-coding:utf-8 -*-

"""
# File       : 109_约会时间差.py
# Time       ：2020/6/14 下午6:59
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""

import random

trial = 100000
total = 0
for i in range(trial):
    A, B = random.random(), random.random()
    total += abs(A-B)
average = total/trial
print(average)