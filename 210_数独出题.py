import random
import turtle
import copy
import mylib.sudoku as sdk
import time
start = time.time()


def get_full_board(matrix, num_base):
    # 初始化棋盘并随机填入若干个满足数独规则的数字（一般小于11个）
    for loops in range(num_base):
        i, j = random.randint(0, 8), random.randint(0, 8)
        choices = sdk.values(matrix, i, j)
        if choices:
            matrix[i][j] = random.choice(choices)
    # 调用求解子程序，获得一个数独终盘
    if sdk.sudoku(matrix):
        return True
    else:
        print("生成终盘失败，请重新尝试。")
        return False


def dig_holes(tries):
    # 挖洞，每欲挖走一个，先测试除了原来数之外的其他数字是否能得到解
    for loops in range(tries):
        i, j = random.randint(0, 8), random.randint(0, 8)
        if board[i][j] == 0:
            continue
        possible = sdk.values(board, i, j)
        unique = True
        for num in possible:
            temp_board = copy.deepcopy(board)
            temp_board[i][j] = num
            if sdk.sudoku(temp_board):
                unique = False
                break
        if unique:
            answer[i][j] = board[i][j]
            board[i][j] = 0


def draw_grid(step=50):
    x0, y0 = -step * 4.5, step * 4.5
    # 画竖线
    for i in range(10):
        x = x0 + i * step
        tt.penup()
        tt.goto(x, y0)
        tt.pendown()
        tt.pensize(2 if i%3 == 0 else 1)
        tt.sety(-y0)
    # 画横线
    for i in range(10):
        y = -y0 + i * step
        tt.penup()
        tt.goto(x0, y)
        tt.pendown()
        tt.pensize(2 if i % 3 == 0 else 1)
        tt.setx(-x0)


def show_sudoku(matrix, step=50):
    x0, y0 = -step * 4 - 5, step * 4 - 15
    for i in range(9):
        y = y0 - i * step
        for j in range(9):
            x = x0 + j * step
            tt.goto(x, y)
            if matrix[i][j] != 0:
                tt.write(matrix[i][j], font=('Arial', 24, 'normal'))


def show_answer(x, y):
    if x > 220 and y < -220:
        show_sudoku(answer)


# ================主程序从这里开始===================

# 第一步，生成终盘
board = [[0 for i in range(9)] for j in range(9)]
answer = [[0 for i in range(9)] for j in range(9)]
while True:
    if get_full_board(board, num_base=7):
        break
for raw in board:
    print(raw)

# 第二步，挖洞并计算难度
dig_holes(99)
level = 0
for raw in range(9):
    for col in range(9):
        if board[raw][col] == 0:
            level += len(sdk.values(board, raw, col))
print("难度系数：", level)

# 记录生成数独盘所花的总时间
end = time.time()
print("花费时间：", end-start)

# 用Turtle画格子，并显示数独盘
turtle.tracer(False)
tt = turtle.Turtle()
draw_grid(step=50)
tt.write('   难度：' + str(level), font=('Arial', 12, 'normal'))
tt.penup()
show_sudoku(board)

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