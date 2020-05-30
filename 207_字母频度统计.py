import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'    # 允许显示中文字体

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
f = open("data/Pride-and-Prejudice-by-Jane-Austen.txt")
stats = {ch: 0 for ch in letters}           # 初始化每个字母的计数为0

while True:
    chars = f.read(4096)                    # 每次读取的字符数，可以调整优化
    if chars == '':                         # 读到空字符表明文件已经读取完毕
        break
    chars = chars.lower()
    for ch in letters:
        stats[ch] += chars.count(ch)

f.close()
print(stats)

plt.bar(stats.keys(), stats.values())
plt.title('字母频度统计', fontdict = {'fontsize': 24})
plt.xlabel('字母', fontdict = {'fontsize': 12})
plt.ylabel('字母出现次数', fontdict = {'fontsize': 12})
plt.show()
