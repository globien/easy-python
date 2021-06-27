# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python


import turtle
turtle.bgcolor('whitesmoke')
leo = turtle.Turtle()
leo.color('red')
leo.shape('turtle')
for length in range(5, 5 * 31, 5):
    leo.right(90)
    leo.forward(length)
turtle.done()

