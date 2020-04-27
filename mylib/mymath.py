# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 计算最大公约数和最小公倍数

def greatest_common_divisor(m,n):
    while m!=n:
        if m > n :
            m = m - n
        else:
            n = n - m
    return m

def least_common_multiple(m,n):
    return m * n // greatest_common_divisor(m,n)

if __name__ == "__main__" :
    m,n = eval(input('请输入两个正整数（逗号隔开）：'))
    print('m =',m, ', n =',n)
    print('它们的最大公约数是：', greatest_common_divisor(m,n))
    print('它们的最小公倍数是：', least_common_multiple(m,n))
