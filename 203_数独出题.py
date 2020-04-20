import random
import turtle


def draw_grid(step=50):
    # 画竖线
    x0 = -step * 4.5
    y0 = step * 4.5
    for i in range(10):
        x = x0 + i * step
        y = y0
        tt.penup()
        tt.goto(x, y)
        y = -y0
        tt.pendown()
        if i % 3 == 0:
            tt.pensize(2)
        else:
            tt.pensize(1)
        tt.goto(x, y)

    # 画横线
    x0 = -step * 4.5
    y0 = step * 4.5
    for i in range(10):
        x = x0
        y = y0 - i * step
        tt.penup()
        tt.goto(x, y)
        x = -x0
        tt.pendown()
        if i % 3 == 0:
            tt.pensize(2)
        else:
            tt.pensize(1)
        tt.goto(x, y)


def show_sudoku(step=50, full=False):
    x0 = -step * 4 - 5
    y0 = step * 4 - 15
    for i in range(9):
        y = y0 - i * step
        for j in range(9):
            x = x0 + j * step
            tt.goto(x, y)
            if not (full) and random.random() < 0.618:
                continue
            tt.write(str(sudoku[i][j]), font=('Arial', 24))


def show_answer(x, y):
    if x > 220 and y < -220:
        show_sudoku(step=50, full=True)


# 主程序从这里开始

# 用随机数按既定模式生成数独终盘
a = random.sample(range(1, 10), 9)
sudoku = [[a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]],
          [a[3], a[4], a[5], a[6], a[7], a[8], a[0], a[1], a[2]],
          [a[6], a[7], a[8], a[0], a[1], a[2], a[3], a[4], a[5]],
          [a[1], a[2], a[0], a[4], a[5], a[3], a[7], a[8], a[6]],
          [a[4], a[5], a[3], a[7], a[8], a[6], a[1], a[2], a[0]],
          [a[7], a[8], a[6], a[1], a[2], a[0], a[4], a[5], a[3]],
          [a[2], a[0], a[1], a[5], a[3], a[4], a[8], a[6], a[7]],
          [a[5], a[3], a[4], a[8], a[6], a[7], a[2], a[0], a[1]],
          [a[8], a[6], a[7], a[2], a[0], a[1], a[5], a[3], a[4]]]

# 用Turtle画格子及显示数独数字
tt = turtle.Turtle()
tt.hideturtle()
tt.speed(0)
turtle.tracer(False)
draw_grid(step=50)
tt.penup()
show_sudoku()

# 画显示答案的提示区域
tt.goto(247, -268)
tt.color('darkred')
tt.write("点这里\n看答案", font=('Arial', 16))
tt.goto(270, -280)
tt.pendown()
tt.circle(30)

# 接收鼠标事件，显示答案
tt.penup()
turtle.onscreenclick(show_answer)

turtle.done()
