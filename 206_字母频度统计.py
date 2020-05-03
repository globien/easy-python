

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
f = open("data/Pride-and-Prejudice-by-Jane-Austen.txt")
stat = {ch: 0 for ch in letters}        # 初始化每个字母的计算为0
'''while True:
    char = f.read(1)
    if char == '':                          # 读到空字符表明文件已经读取完毕
        break
    char = char.lower()
    if char in letters:
        stat[char] += 1'''

while True:
    chars = f.read(4096)            # 每次读取的字符数，可以调整优化
    if chars == '':                 # 读到空字符表明文件已经读取完毕
        break
    chars = chars.lower()
    for ch in letters:
        stat[ch] += chars.count(ch)


print(stat)
f.close()
