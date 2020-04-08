import turtle
from math import *
from B02a_最大公约数最小公倍数 import *

r = 25
R = 120
d = 50

flower = turtle.Turtle()
flower.penup()
flower.color("orange")
flower.pensize("2")
flower.begin_fill()
theta = 0
while theta < 2 * pi * least_common_multiple(r, R)/R:
    x = (R-r) * cos(theta) + d * cos((R - r) / r * theta)
    y = (R-r) * sin(theta) - d * sin((R - r) / r * theta)
    flower.goto(x, y)
    flower.pendown()
    theta += 0.05
flower.hideturtle()
flower.end_fill()
turtle.done()

