# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# Python巨蟒超级计算器 (version 1.0 beta)
# 可以做超级大的整数运算，例如计算10000的阶乘或365的10000次方毫无压力，如果你真的需要这样做的话

from math import *

# 自定义函数，打印提示信息，主程序将在启动和用户输入出错时调用
def print_prompt():
    print("- 可使用 + - * / 及 %(模除) 和 //(整除)等符号")
    print("- 可使用小括号表示计算优先级，并且可以嵌套使用")
    print("- 乘方可用**或pow(x,y)函数表示，如3**2表示3的平方")
    print("- 开平方可用sqrt(x)函数，如sqrt(3)表示3的平方根")
    print("- 求对数用log(x,b)函数，b是底数，可省略表示底为e")
    print("- 可以使用三角函数及符号pi，如sin(pi)表示求sinπ")
    print("- 阶乘使用factorial(x)，如factorial(3)表示3的阶乘")
    print("- 要退出程序请输入q或quit")
    print()

#主程序从这里开始
print("Python巨蟒超级计算器 version 1.0 beta\n")
print_prompt()
while 1:                    # 反复运行直到用户明确指示退出
    exp = input("请输入算式:\n")
    if exp[0] == "q" or exp[0] == "Q":
        print("程序已根据您的要求退出。")
        break
    try:
        x = eval(exp)       # eval()函数把字符串转换为表达式
    except:
        print("算式有错，请仔细检查。")
        print_prompt()
    else:
        print("=", x)
        print()
