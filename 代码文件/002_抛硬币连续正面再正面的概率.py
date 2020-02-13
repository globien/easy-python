# 验证抛硬币出现N次连续正面后，下一次还是正面的概率是不是50%

import random

EXP_NUM = 100000    # 总的实验次数
N = 3               # 我们将观察连续出现N次正面后会发生什么
counter1 = 0        # 统计共多少次出现连续正面
counter2 = 0        # 统计出现连续正面后，再一次出现正面的次数

for i in range(EXP_NUM):
    counter3 = 0                        # 用来统计是否连续正面
    for j in range(N):
        coin = random.randint(0,1)
        counter3 = counter3 + coin      # 累计出现正面的次数
    if counter3 == N:                   # 表明连续出现了N次正面
        counter1 = counter1 + 1
        counter2 = counter2 + random.randint(0,1)  # 再扔一次

print("连续出现N次正面的总次数", counter1)
print("连续出现N次正面后，再次出现正面的次数", counter2)
print("连续出现N次正面后，再次出现正面的比例", counter2/counter1)

# 详述文件：https://github.com/globien/easy_python/blob/master/描述文件/002_抛硬币连续正面再正面的概率.md
