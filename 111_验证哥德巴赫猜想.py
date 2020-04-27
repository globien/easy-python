# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 哥德巴赫猜想：任何一个大于2的偶数都可以表示为两个素数之和
# 本程序在普通家用计算机上可以验证最大大约至4000000000000000（15个零）的偶数
# 用试除法判断一个数是否为素数, 即：用小于该数的每个整数去除它，挨个验证能否整除
# 试除法所需验证的因子不需超过目标整数的平方根

# 判断一个整数是不是素数
def is_prime(n):
    if n < 2 :
        return False
    if n == 2 :
        return True
    if n % 2 == 0:             # 偶数显然不是素数
        return False
    div = 3                         # 从3开始，验证number有没有整除因子
    while div * div <= n:      # 需验证的因子不需要超过目标数的平方根
        if n % div == 0:
            return False
        else:
            div += 2
    return True

# 输入想验证的起始偶数
while 1:
    first = int(input("请输入一个大于等于4的偶数："))
    if first < 4 or first % 2 != 0:
        print("你的输入有误，请重新输入。\n")
    else:
        break

# 连续验算N个偶数        
N = 10
if first == 4:
    print("4 : 2 + 2")                  # 已知4符合歌德巴赫猜想，直接给结果
    N -= 1
    first = 6
for i in range(N):
    even_num = first + 2 * i
    print(even_num, ": ", end="")
    j = 3
    while j <= even_num//2 :                 # 从3开始验证每对奇数j和num-j
        if is_prime(j) and is_prime(even_num - j):
            print(j, "+", even_num - j)
            break
        j += 2
    if j > even_num//2 :             # 说明上面的while循环结束了也没找到结果
        print(even_num, "：没找到'1+1'结构，恭喜你推翻了哥德巴赫猜想！！！")
