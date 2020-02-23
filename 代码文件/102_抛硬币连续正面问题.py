# 验证抛硬币出现N次连续正面后，下一次还是正面的概率是不是50%

import random

N = 3               # 我们将观察连续出现N次正面后会发生什么
EXP_NUM = 150000    # 总的抛硬币次数

counter1 = 0        # 用来统计已经连续几次正面了
counter2 = 0        # 统计共多少次出现连续N次正面
counter3 = 0        # 统计出现连续N次正面后，再一次出现正面的次数

for i in range(EXP_NUM):
    coin = random.randint(0,1)
    if coin == 1:                       # 扔到了一次正面
        counter1 = counter1 + 1         # 累计出现正面的次数          
    else:
        counter1 = 0                    # 不是正面，重置计数器        
    
    if counter1 == N:                   # 表明连续出现了N次正面
        counter2 = counter2 + 1         # 累计出现N次正面的次数
        counter3 = counter3 + random.randint(0,1)  # 再扔一次，累计连续N次正面后再次正面的次数
        counter1 = 0                    # 重置计数器，准备下一次实验
        
print("N =", N)
print("EXP_NUM = ", EXP_NUM)
print("连续出现N次正面的总次数", counter2)
print("连续出现N次正面后，再次出现正面的次数", counter3)
print("连续出现N次正面后，再次出现正面的比例", counter3/counter2)

# 详述文件：https://github.com/globien/easy_python/blob/master/描述文件/102_抛硬币连续正面问题.md
