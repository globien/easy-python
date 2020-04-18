import turtle
from random import *
from mylib.myflowers import *                               # 导入自定义的画花的函数库

win = turtle.Screen()
win.bgcolor('#8A5370')                                      # 背景设为深紫色
tt = turtle.Turtle()
color_table = ['#EBD6D9', '#C46C98', '#DB91B2']
size_table = [1, 1, 1, 1, 2, 2, 2, 3, 4]

N = 25                                                      # 一共画N朵樱花
for i in range(N):
    size = size_table[randint(0,len(size_table)-1)]         # 随机选择一种花瓣大小
    color = color_table[randint(0,len(color_table)-1)]      # 随机选择一种花瓣颜色
    angle = pi * random()                                   # 随机选择花瓣方向
    x0 = randint(0, 600) - 300                              # 随机选择位置横坐标
    y0 = randint(0, 600) - 300                              # 随机位置纵坐标
    sakura(tt, size, x0, y0, angle, color, 'fastest')       # 调用自定义画花函数库中的"樱花"函数

tt.hideturtle()                                             # 隐藏海龟箭头
turtle.done()
