# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python
# 暴力验证哥德巴赫猜想：任何一个大偶数都可以表示为两个素数之和
# 普通家用计算机上大约可以验证到1000000000000000（15个零）的大偶数
# 用试除法判断一个整数是否为素数, 试除法所需验证的因子不需超过目标整数的平方根

def is_prime(number):
    if number % 2 == 0:                 # 偶数显然不是素数，这里我们不考虑2本身
        return False
    factor = 3
    while factor * factor <= number :   # 需验证的因子不需要超过目标数的平方根
        if number % factor == 0:
            return False
        else:
            factor += 2
    return True

# 输入想验证的起始偶数
while 1:
    first = int(input("请输入一个大于等于6的偶数："))
    if first % 2 == 0 and first >= 6 :
        break
    else:
        print("你的输入有误，请重新输入。\n")

# 连续验算N个偶数        
N = 10                  
for i in range(N):
    num = first + 2 * i
    result = False
    for j in range(3, num//2, 2):             # 从3开始验证每对奇数j和num-j
        if is_prime(j) and is_prime(num - j):
            print(num, "=", j, "+", num - j)
            result = True
            break
    if result == False :
        print(num, "：没找到'1+1'结构，不符合哥德巴赫猜想！！！")
        
    
