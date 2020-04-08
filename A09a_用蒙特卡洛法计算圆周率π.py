# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python
# 用蒙特卡洛法计算圆周率，即，往一个正方形里扔豆子，计算有多少比例的豆子扔在了该正方形的内切圆中

import random

num_all = 0         #随机点总计数器
num_cir = 0         #随机点在圆内的计数器
num_halt = 10000000 #每产生这么多个随机点后，计算并打印一次目前的结果

print("将进行无限计算，请用Ctrl_C或其他方式强制退出！！！")
input("按回车(Enter)键开始...")
print("开始计算...，退出请用Ctrl_C或其他强制退出方式...")
print("\n实验次数        计算结果")

while 1 :
    for i in range(num_halt): 
        x = random.random()         #获得随机点的横坐标
        y = random.random()         #获得随机点的纵坐标
        if x*x + y*y < 1 :          #随机点(x,y)在圆内
            num_cir = num_cir + 1   #圆内计数器+1
        num_all = num_all + 1       #总计数器+1
    pi = 4*num_cir/num_all
    print(num_all,"   ", pi)

    
