# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 图形计算器（功能尚不完整，可做加减乘除）


def input_calculate(x, y):

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
        temp = get_result()
        clear_all()
        operand[0] = str(temp)
    elif 57 <= x < 118 and -102 <= y < -5:     # key '+' and '-'
        temp = get_result()
        clear_all()
        operand[0] = str(temp)
        operator[0] = '+' if y<-53 else '-'
        operand_pt += 1
        operator_pt += 1
        is_result = False
    elif 57 <= x < 118 and -5 <= y < 90:        # key '*' and '/', 根据情况可能需要先做部分运算
        if operator_pt == 0:
            operator[0] = '*' if y<42 else '/'
            operator_pt = 1
            operand_pt = 1
        elif operator_pt == 1:
            if operator[0] in ['*', '/']:
                get_result()
                operator[0] = '*' if y < 42 else '/'
                operator_pt = 1
                operand_pt = 1
            else:
                operator[1] = '*' if y < 42 else '/'
                operator_pt = 2
                operand_pt = 2
        else:
            operand[1] = str(eval(operand[1] + operator[1] + operand[2]))
            operand[2] = ''
            operator[1] = '*' if y < 42 else '/'
            operand_pt = 2
        is_result = False
    else:                                       # key '+/-' and '%' are not effective
        pass

    tt.clear()
    if operand[operand_pt] == '':
        show_exp(operand[operand_pt-1])
    else:
        show_exp(operand[operand_pt])


def show_exp(expression):
    # 自定义显示结果输入和结果的函数
    tt.write(expression, align='right', font=('Arial', 48, 'normal'))


def get_result():
    result = operand[0] + operator[0] + operand[1] + operator[1] + operand[2]
    print(operand, operator)
    if result[-1] in ['+', '-', '*', '/']:
        result = result[:-1]
    print(result, '= ', end='' )
    result = eval(result)
    print(result)
    return result


def clear_all():
    # 自定义全部清零的函数

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
    show_exp('0')
    turtle.onscreenclick(input_calculate)

    turtle.done()
