# -*-coding:utf-8 -*-

"""
# File       : A010_最长重复字符子串.py
# Time       ：2021-05-10 2:05 下午
# Author     ：Dr. Xianyu
# version    ：python 3.8
# Description：
"""


def longest_run(s):
    first = left = 0
    end = right = 0
    sub_length = 0
    while right < len(s) - 1:
        right += 1
        if s[right] == s[right - 1]:
            if right - left + 1 > sub_length:
                first = left
                end = right
                sub_length = end - first + 1
            else:
                pass      # continue to compare next element
        else:
            left = right
    return first, end


# test = "abbbbbbcdeeefhhhhbbb"

import random
test = [random.randrange(1, 7) for i in range(20)]
longest = longest_run(test)
for i, e in enumerate(test):
    if i == longest[0]:
        print("(", end=" ")
    print(e, end=" ")
    if i == longest[1]:
        print(")", end=" ")



