import random

num_all = 0
num_cir = 0
num_halt = 10000000                                  # 每循环该次数后，打印一次目前的计算结果

print("将进行无限计算，请用Ctrl_C或其他方式强制退出！！！")
input("按任意键开始...")
print("开始计算...，退出请用Ctrl_C或其他强制退出方式...")
print("\n实验次数        计算结果")

while 1 :
    for i in range(num_halt):
        x = random.random()                         # 随机获得横坐标
        y = random.random()                         # 随机获得纵坐标
        if x*x + y*y < 1 :                          # 点(x,y)在圆内
            num_cir = num_cir + 1
        num_all = num_all + 1
    pi = 4*num_cir/num_all
    print(num_all,"   ", pi)
