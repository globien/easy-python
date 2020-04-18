import turtle
from math import *
from random import *
from mylib.mymath import *

def sakura(tt, size = 3, x0 = 0, y0 = 0, angle = 0, color ='#EBD6D9', speed = 'fastest'):

    # 画花瓣
    p = 5
    q = 3
    R = size * 15
    tt.penup()
    tt.color(color)
    tt.pensize("2")
    tt.begin_fill()
    tt.speed(speed)
    theta = 0
    while theta <= pi * q + 0.01:       # 多画0.01弧度避免缺陷
        x = R * cos(p / q * theta + angle) * cos(theta + angle) + x0
        y = R * cos(p / q * theta + angle) * sin(theta + angle) + y0
        tt.goto(x, y)
        tt.pendown()
        theta += pi/R
    tt.penup()
    tt.end_fill()

    # 画花蕊
    tt.color('#B17085')
    tt.begin_fill()
    r = size
    R = size * 5
    d = r * 1.3
    angle = angle * pi/5
    theta = 0
    while theta <= 2 * pi * least_common_multiple(r, R) / R + 0.01:  # 多画0.01弧度避免有缺陷
        x = (R - r) * cos(theta + angle) + d * cos((R - r) / r * theta + angle) + x0
        y = (R - r) * sin(theta + angle) - d * sin((R - r) / r * theta + angle) + y0
        tt.goto(x, y)
        tt.pendown()
        theta += pi / R
    tt.end_fill()
    tt.penup()

if __name__ == '__main__':
    win = turtle.Screen()
    win.bgcolor('#8A5370')
    tt = turtle.Turtle()
    color_table = ['#EBD6D9', '#C46C98', '#DB91B2']
    size_table = [1, 1, 1, 1, 2, 2, 2, 3, 4]
    for i in range(20):
        angle = pi * random()
        size = size_table[randint(0,len(size_table)-1)]
        color = color_table[randint(0,len(color_table)-1)]
        x0 = randint(0, 400) - 200
        y0 = randint(0, 400) - 200
        sakura(tt, size, x0, y0, angle, color, 'fastest')
    tt.hideturtle()
    turtle.done()
