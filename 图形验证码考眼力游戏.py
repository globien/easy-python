import turtle
from random import *

def draw_keys():
    poly_num = randint(3, 6)
    points = [[randint(1,5)*15, randint(2,17)*10] for j in range(poly_num)]
    cor = [[0,0],[0,0]]
    for i in range(2):
        tt.penup()
        cor[i] = [randint(x_min,x_max),randint(y_min,y_max)]
        tt.goto(cor[i][0],cor[i][1])
        tt.pendown()
        tt.begin_fill()
        tt.color(choice(color_table))
        for distance, angle in points:
            tt.right(angle)
            tt.fd(distance)
            cor[i][0] = cor[i][0] + tt.xcor()
            cor[i][1] = cor[i][1] + tt.ycor()
        tt.end_fill()
        cor[i][0] = cor[i][0] / (poly_num + 1)
        cor[i][1] = cor[i][1] / (poly_num + 1)
        tt.penup()
        tt.goto(cor[i][0],cor[i][1])


def draw_others():
    N = 7                   # 生成的干扰图形个数，加大此数就意味着加大难度
    for i in range(N):
        tt.penup()
        tt.goto(randint(x_min,x_max),randint(y_min,y_max))
        poly_num = randint(3, 6)
        points = [[randint(1,5)*15, randint(2,17)*10] for j in range(poly_num)]
        tt.begin_fill()
        tt.pendown()
        tt.color(choice(color_table))
        for distance, angle in points:
            tt.right(angle)
            tt.fd(distance)
        tt.end_fill()


def draw_turtle():
    tt.penup()
    tt.color('olive')
    tt.goto(-250, -250)
    turtle.tracer(True)
    tt.speed('fastest')
    tt.setheading(45)
    tt.shape('turtle')
    tt.resizemode('user')
    tt.shapesize(3, 3)

def draw_button(word, x0, y0):
    tt.color('red')
    tt.pensize(2)
    tt.penup()
    tt.goto(x0, y0)
    tt.setheading(90)
    tt.pendown()
    tt.fd(35)
    tt.right(90)
    tt.fd(105)
    tt.right(90)
    tt.fd(35)
    tt.right(90)
    tt.fd(105)
    tt.write(word, font=('Arial',30, 'normal'))


if __name__ == '__main__':
    turtle.tracer(False)
    tt = turtle.Turtle()
    tt.penup()
    tt.goto(0,270)
    tt.write("此处有两个形状完全相同的图形(颜色和方向可能不同)，请把海龟拉到其中一个上后确认", align='center', font=('Arial', 16, 'normal'))
    color_table = ['red','orange','brown','green','blue','purple','silver','gold']
    x_min, x_max, y_min, y_max = -170, 180, -170, 180             # 限定图形出现的范围

    draw_keys()
    draw_others()
    draw_button('  确  认', -130, -270)
    draw_button('  重  置',   40, -270)
    draw_turtle()


    tt.ondrag(tt.goto)  # 把goto函数绑定到鼠标拖动事件上
    turtle.done()