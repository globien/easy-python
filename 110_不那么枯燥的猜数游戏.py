# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python
# 不那么枯燥的猜数游戏

import random

very_happy = "小蟒今天开心极了，你来猜猜我的心情指数？"
happy = "小蟒现在挺高兴，你猜猜我的心情指数是多少？"
so_so = "小蟒现在感觉还行吧，你想知道我的心情指数是多少吗？"
sad = "小蟒现在不太高兴，你猜猜我的心情指数吧。"
very_sad = "小蟒今天很不开心，要猜你就猜小一点的数字吧。"
level_list = [very_sad, sad, so_so, happy, very_happy]

level = random.randint(0,4)
emotion = level * 20 + random.randint(1,20)
print(level_list[level])

guess = int(input("请输入1~100的数字："))
n = 1                       # 已经猜的次数
while guess != emotion:
    if guess - emotion > 10: print("你猜得太大了！！！")
    elif guess - emotion > 0: print("大了一点点，加油！")
    elif guess - emotion < -10: print("你猜得太小了！！！")
    else: print("猜得小了一点，继续！")
    guess = int(input("请重新输入你的猜测："))
    n = n + 1
    
if n < 5: 
    print("恭喜你", n, "次就猜对了！智商杠杠的！")
else: 
    print("恭喜你终于猜对了，你猜了", n, "次。加油喔！")
    
    
