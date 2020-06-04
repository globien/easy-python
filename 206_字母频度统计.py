# 研究QWERTY键盘的设计原理，与原发明肖尔斯键盘的比较
# 作者：西岛闲鱼

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'                # 允许显示中文字体

# QWERTY键盘
row = (('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'),
       ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'),
       ('z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?'))

# 肖尔斯键盘
'''row = (('q', 'w', 'e', '.', 't', 'y', 'i', 'u', 'o', 'p')
       ('z', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm')
       ('a', 'x', '&', 'c', 'v', 'b', 'n', '?', ';', 'r'))'''

stats = [{ch: 0 for ch in row[i]} for i in range(3)]    # 初始化第一排每个字母的计数为0

f = open("data/Pride-and-Prejudice-by-Jane-Austen.txt")
while True:
    chars = f.read(4096)                                # 每次读取的字符数，可以调整优化
    if chars == '':                                     # 读到空字符表明文件已经读取完毕
        break
    chars = chars.lower()
    for i in range(3):
        for ch in row[i]:
            stats[i][ch] += chars.count(ch)

f.close()

for i in range(3):
    plt.bar(stats[i].keys(), stats[i].values())
plt.title('键盘字母频度统计', fontdict = {'fontsize': 18})
plt.xlabel('字母/键位', fontdict = {'fontsize': 12})
plt.ylabel('字母/键位出现次数', fontdict = {'fontsize': 12})
plt.show()
