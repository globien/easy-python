words = []
while True:
    word = input()
    if word == '':
        break
    elif word in words:
        pass
    else:
        words.append(word)

for word in words:
    print(word)
