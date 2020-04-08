import turtle
for length in range(5,5*31,5):
    turtle.right(90)
    turtle.fd(length)
turtle.done()


from math import *
def greatest_common_divisor(m,n):
    while m!=n:
        if m > n :
            m = m - n
        else:
            n = n - m
    return m

def least_common_multiple(m,n):
    return m * n // greatest_common_divisor(m,n)

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

