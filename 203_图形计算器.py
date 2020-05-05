# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 图形计算器（功能尚不完整，可做加减乘除，没有正负变换和百分号功能）


def get_inputs(x, y):
    # 把以下变量声明为全局变量，以便可以在函数内修改它们
    global operand
    global operator
    global operand_pt
    global operator_pt
    global is_result

    if -115 <= x < -59 and 42 <= y < 90:        # key 'AC'
        clear_all()
    elif -115 <= x < -1 and -150 <= y < -102:   # key '0'
        if is_result:
            clear_all()
        else:
            operand[operand_pt] += '0'
    elif -1 <= x < 57 and -150 <= y < -102:     # key '.'
        if '.' not in operand[operand_pt]:
            if is_result:
                clear_all()
            operand[operand_pt] += '.'
            is_result = False
    elif -115 <= x < 57 and -102 <= y < 42:     # key '1~9'
        if is_result:
            clear_all()
            operand[0] = ''
        digit = int(x + 115) // 57 + 1 + int(y + 102) // 48 * 3
        operand[operand_pt] += str(digit)
        is_result = False
    elif 57 <= x < 118 and -150 <= y < -102:    # key '='
        operand[0] = get_result()
    elif 57 <= x < 118 and -102 <= y < -5:      # key '+' and '-'
        operand[0] = get_result()
        operator[0] = '+' if y<-53 else '-'
        operand_pt += 1
        operator_pt += 1
        is_result = False
    elif 57 <= x < 118 and -5 <= y < 90:        # key '*' and '/', 根据情况可能需要先做部分运算
        if operator_pt == 0:
            operator[0] = '*' if y < 42 else '/'
            operator_pt = operand_pt = 1
        elif operator_pt == 1:
            if operator[0] in ['*', '/']:       # 前面是乘除号，先计算前面的结果
                operand[0] = get_result()
                operator[0] = '*' if y < 42 else '/'
                operator_pt = operand_pt = 1
            else:                               # 前面是加减号，暂不做计算
                operator[1] = '*' if y < 42 else '/'
                operator_pt = operand_pt = 2
        else:                                    # operator_pt == 2，即按下了第三个算符，需要立即做部分运算
            operand[1] = get_result(partial=True)
            operand[2] = ''
            operator[1] = '*' if y < 42 else '/'
            operand_pt = 2
        is_result = False
    else:                                       # key '+/-' and '%' are not effective
        pass

    # 每次按键都刷新显示最新的数字
    tt.clear()
    if operand[operand_pt] == '':
        display(operand[operand_pt - 1])        # 当前位置没有输入新的数字，只计算前面的表达式并显示，但要保留最后一个算符
    else:
        display(operand[operand_pt])            # 计算全部表达式并显示


def get_result(partial=False):
    # 计算并返回一个表达式的结果
    if partial:
        exp = operand[1] + operator[1] + operand[2]
    else:
        exp = operand[0] + operator[0] + operand[1] + operator[1] + operand[2]
        clear_all()
    if exp[-1] in ['+', '-', '*', '/']:
        exp = exp[:-1]                          # 结尾如果是一个运算符，它不参与运算
    try:
        result = '%g' % eval(exp)               # 根据结果大小决定是否使用科学记数法
    except:
        result = 'Error'
    return result


def display(number):
    # 显示输入的数字或运算结果
    tt.write(number, align='right', font=('Arial', 32, 'normal'))
    if number == 'Error':
        clear_all()


def clear_all():
    # 把以下变量声明为全局变量，以便可以在函数内修改它们
    global operand
    global operator
    global operand_pt
    global operator_pt
    global is_result
    # 初始化输入数据和状态，保存最多3个数和最多2个运算符，以及各自目前的指向位置
    operand = ['0', '', '']
    operator = ['', '']
    operand_pt = 0
    operator_pt = 0
    is_result = True


if __name__ == '__main__':
    import turtle

    # 初始化数据部分
    operand = operator = []
    operand_pt = operator_pt = 0
    is_result = True
    clear_all()

    # 初始化显示部分，并等待屏幕点击，然后调用自定义函数处理每一次点击
    turtle.setup(420, 500)
    turtle.bgpic('img/图形计算器.png')
    tt = turtle.Turtle()
    tt.hideturtle()
    tt.penup()
    tt.color('white')
    tt.goto(102, 90)
    display('0')
    turtle.onscreenclick(get_inputs)

    turtle.done()
