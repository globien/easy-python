import turtle
from math import *
from mylib.mymath import *

r = 25
R = 120
d = 50

flower = turtle.Turtle()
flower.speed(0)
flower.penup()
flower.color("orange")
flower.pensize("2")
flower.begin_fill()
theta = 0
while theta <= 2 * pi * least_common_multiple(r, R)/R + 0.01:  # 多画0.01弧度避免有缺陷
    x = (R-r) * cos(theta) + d * cos((R - r) / r * theta)
    y = (R-r) * sin(theta) - d * sin((R - r) / r * theta)
    flower.goto(x, y)
    flower.pendown()
    theta += pi/100
flower.hideturtle()
flower.end_fill()
turtle.done()

