# -*-coding:utf-8 -*-

"""
# File       : 304_多个数的最大公约数.py
# Time       ：2021-03-26 10:51 上午
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""

from mylib.mymath import *
import random

def multi_gcd(array):
    l = len(array)
    if l == 1:
        return array[0]
    elif l == 2:
        return greatest_common_divisor(array[0], array[1])
    else:
        return greatest_common_divisor(multi_gcd(array[:l//2]), multi_gcd(array[l//2:]))


a = [39 * random.choice(range(1, 30)) for i in range(21)]
print(a)
print(multi_gcd(a))
