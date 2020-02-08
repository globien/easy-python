
import random
获奖次数_不换 = 0 #不换
获奖次数_换 = 0 #换
试验次数 = 100000 

for i in range(试验次数):
    door_list = [1,2,3,4]
    car = random.choice(door_list)                          #汽车随机出现在三扇门之中
    choice1 = random.choice(door_list)                #挑战者随机选择了一扇门
    if choice1 == car:
        获奖次数_不换 = 获奖次数_不换 + 1                       #如果挑战者一开始选的门背后有汽车，那么不换可获奖
    
    #主持人随机选择一扇门，这扇门不是挑战者选择的门，也不是汽车所在的门; 连续做两次
    door_list.remove(choice1)
    if car in door_list:
        door_list.remove(car)
    discard1 = random.choice(door_list)

    door_list = [1,2,3,4]
    door_list.remove(choice1)
    door_list.remove(discard1)
    choice2 = random.choice(door_list)

    door_list = [1,2,3,4]
    door_list.remove(choice2)
    door_list.remove(discard1)
    if car in door_list:
        door_list.remove(car)
    discard2 = random.choice(door_list)

    door_list = [1,2,3,4]
    door_list.remove(choice2)
    door_list.remove(discard1)
    door_list.remove(discard2)
    choice3 = random.choice(door_list)

    if choice3 == car:
        获奖次数_换 = 获奖次数_换 + 1                  #如果挑战者一开始选的门背后没有汽车，那么换可获奖

print(获奖次数_不换/试验次数)
print(获奖次数_换/试验次数)
