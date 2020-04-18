from math import *
from mylib.mymath import *              # 导入自定义的数学函数库

# 自定义太阳花函数
def sunflower(tt, color = 'orange'):
    r = 25
    R = 120
    d = 50
    tt.penup()
    tt.color(color)
    tt.pensize("2")
    tt.begin_fill()
    theta = 0
    while theta <= 2 * pi * least_common_multiple(r, R)/R + 0.01:  # 多画0.01弧度避免有缺陷
        x = (R-r) * cos(theta) + d * cos((R - r) / r * theta)
        y = (R-r) * sin(theta) - d * sin((R - r) / r * theta)
        tt.goto(x, y)
        tt.pendown()
        theta += pi/100
    tt.end_fill()



# 自定义樱花函数
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


if __name__ == '__main__':                          # 测试用，仅在本文件为主程序时，才会执行下面的代码
    import turtle
    tt = turtle.Turtle()
    sunflower(tt,'orange')

    win = turtle.Screen()
    win.bgcolor('#8A5370')
    sakura(tt, 3, 0, 0, 0, "pink", 'fastest')

    tt.hideturtle()
    turtle.done()