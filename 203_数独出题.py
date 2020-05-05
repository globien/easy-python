# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

from random import *
import turtle


def draw_grid(step=50):
    x0 = -step * 4.5
    y0 = step * 4.5
    # 画竖线
    for i in range(10):
        x = x0 + i * step
        tt.penup()
        tt.goto(x, y0)
        tt.pendown()
        tt.pensize(2 if i%3==0 else 1)
        tt.sety(-y0)
    # 画横线
    for i in range(10):
        y = y0 - i * step
        tt.penup()
        tt.goto(x0, y)
        tt.pendown()
        tt.pensize(2 if i % 3 == 0 else 1)
        tt.setx(-x0)


def get_holes(quarter_holes_num):
    holes_seq = sample(range(1, 25), quarter_holes_num)      # 随机决定25个格子里（四分之一个数独盘），哪些格子将被挖掉
    holes = []
    n = 0
    for i in range(9):
        ii = min(i, 8 - i)
        for j in range(ii + 1):
            n += 1
            if n in holes_seq:
                holes[len(holes):] = [[i, j], [j, i], [8 - i, 8 - j], [8 - j, 8 - i]]   # 每次产生4个位置对称的洞，附加到holes列表后面
    return holes


def show_sudoku(step=50, full=False):
    x0 = -step * 4 - 5
    y0 = step * 4 - 15
    for i in range(9):
        y = y0 - i * step
        for j in range(9):
            x = x0 + j * step
            tt.goto(x, y)
            if not full:
                if [i, j] not in holes:
                    tt.write(str(sudoku[i][j]), font=('Arial', 24, 'normal'))
            else:
                if [i, j] in holes:
                    tt.write(str(sudoku[i][j]), font=('Arial', 24, 'normal'))


def show_answer(x, y):
    if x > 220 and y < -220:
        show_sudoku(step=50, full=True)


# 主程序从这里开始

# 用双重随机方法，从一个终盘种子生成数十亿种数独终盘。
# 修改种子盘可以生成新的数十亿种终盘。修改时注意seed中a的角标为数独对应位置数减1。
a = sample(range(1, 10), 9)
seed = [[a[1], a[2], a[7], a[0], a[4], a[6], a[3], a[5], a[8]],
        [a[0], a[3], a[4], a[7], a[8], a[5], a[2], a[1], a[6]],
        [a[6], a[5], a[8], a[3], a[1], a[2], a[7], a[0], a[4]],
        [a[5], a[7], a[2], a[1], a[0], a[8], a[6], a[4], a[3]],
        [a[3], a[6], a[0], a[4], a[2], a[7], a[5], a[8], a[1]],
        [a[4], a[8], a[1], a[6], a[5], a[3], a[0], a[7], a[2]],
        [a[2], a[4], a[5], a[8], a[3], a[0], a[1], a[6], a[7]],
        [a[7], a[1], a[3], a[5], a[6], a[4], a[8], a[2], a[0]],
        [a[8], a[0], a[6], a[2], a[7], a[1], a[4], a[3], a[5]]]
m = sample(range(0, 3), 3) + sample(range(3, 6), 3) + sample(range(6, 9), 3)
n = sample(range(0, 3), 3) + sample(range(3, 6), 3) + sample(range(6, 9), 3)
sudoku = [[0] * 9 for i in range(9)]        # 初始化数独矩阵
for i in range(9):
    for j in range(9):
        sudoku[i][j] = seed[m[i]][n[j]]     # 产生数独矩阵终盘

# 用Turtle画格子，以及显示上述数独盘的提示数（即挖去一些洞）
turtle.tracer(False)
tt = turtle.Turtle()
tt.speed(0)
draw_grid(step=50)
holes = get_holes(quarter_holes_num=14)
tt.penup()
show_sudoku()

# 画出显示答案的按钮区域
tt.goto(247, -268)
tt.color('FireBrick')
tt.write("点这里\n看答案", font=('Arial', 16, 'normal'))
tt.goto(270, -280)
tt.pendown()
tt.circle(30)

# 接收鼠标事件，显示答案
tt.penup()
turtle.onscreenclick(show_answer)

turtle.done()

