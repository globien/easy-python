def assign(num_persons, level: "车的级别，大巴为3，中巴2，小巴1，的士0"):
    if num_persons < 10 or level == 0:              # 递归的结束条件：剩余人数少于10，或已经递归到第0级
        count[0] = num_persons                      # 剩余人数小于10人，都坐的士
        return                                      # 递归结束
    count[level] = num_persons // seats[level]      # 尽量坐满本级别的车
    remain = num_persons % seats[level]             # 本级别车坐满后，剩余的人数
    if remain >= (price[level] - price[level - 1])/price[0] + seats[level - 1]:
        count[level] += 1                           # 剩余人数较多，即使坐不满，再派一辆本级别的车也是合算的
        return                                      # 已经分配完毕，递归也结束
    else:
        assign(remain, level - 1)                   # 剩余人数太少，坐本级别的车不合算时，递归调用下一级车分配


seats = (1, 40, 60, 80)
price = (220, 2200, 2600, 3000)
for i in range(1,1001):
    count = [0, 0, 0, 0]                            # 每种车需要的数量，初始化
    assign(i, level=3)                              # 从大巴车（级别为3）开始分配
    print("总人数:", i, "    大巴:", count[3], "    中巴:", count[2], "    小巴:", count[1], "    的士:", count[0])
