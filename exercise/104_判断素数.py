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

num = int(input('请输入一个正整数：'))
if is_prime(num):
    print('Bingo!', num, '是素数!')
else:
    while True:
        num += 1
        if is_prime(num):
            print('大于输入整数的第一个素数是：', num)
            break