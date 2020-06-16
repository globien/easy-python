# -*-coding:utf-8 -*-

"""
# File       :  线性插值函数.py
# Time       ：  2020/6/10 上午9:49
# Author     ：  Dr. Xianyu
# version    ：  python 3.8
# Description：  y是x的函数，分别以列表表示。x单调递增。new_x也是递增，且所有元素在x最大值最小值范围内。
                计算并返回new_y，是new_x对应的函数值，（new_x,new_y)每个点落在最近的x与y连成的直线上。
"""

import numpy
def linear_interpolate(x, y, x_new):
    # x, y, x_new are lists and all sorted
    # return the linear interpolate value for every element of x_new
    y_new = []
    x_temp = numpy.array(x)
    for x_p in x_new:
        n = x_temp.searchsorted(x_p)        # 定位：x_p位于x[n-1]和x[n]之间
        k = (y[n]-y[n-1])/(x[n]-x[n-1])     # 斜率
        y_new.append(k * (x_p-x[n-1]) + y[n-1])
    return y_new


if __name__ == '__main__':
    x = [0, 1, 2]
    y = [2, 1, 3]
    x_new = [0.5, 1.5]
    print(linear_interpolate(x,y,x_new))