import random
import matplotlib.pyplot as plt

trial = 20                  # 模拟实验次数
amp = 2.0                   # 上下振幅（对称乘除）

cash = 1.0                  # 初始现金
days = 200                  # 每次模拟实验观察天数

print("\n多次实验，每次实验的最终股价与总资产的对比：\n")
for i in range(trial):
    money = value = cash / 2    # 一半买为股票，一半保留现金
    price = 1.0                 # 初始股票价格
    shares = value / price      # 初始买的股票数，假定允许买卖分数股数

    moneys = [money]            # 数组，用来存放每天的现金额
    values = [value]            # 数组，用来存放每天的股票市值
    prices = [price]            # 数组，用来存放每天的股票价格
    assets = [money + value]    # 数组，用来存放每天的总资产

    for day in range(1, days):
        price = price * amp**random.choice([-1,1])    # 随机决定上涨还是下跌
        prices.append(price)
        val_tmp = shares * price
        delta = (val_tmp - money) / price / 2   # 卖出/买入股值与现金的差值一半对应的股票，保持股值与现金相等
        shares = shares - delta
        value = shares * price
        values.append(value)
        money = money + delta * price
        moneys.append(money)
        assets.append(money + value)
    print("第{:2d}次实验结果： Price = {:.2e}   Assets = {:.2e}    A/P = {:.2e}".format(i+1, prices[days-1],assets[days-1],assets[days-1]/prices[days-1]))


# 把最后一次实验数据用走势图展示出来
plt.plot(range(days), prices, label='Stock Price')      # 对价格按日期作图（折线图）
plt.plot(range(days), assets, label='Total Assets')     # 对资产按日期作图（折线图）
plt.xlabel('Days')                                      # 横坐标名称
plt.ylabel('Total Assets / Stock Price')                # 纵坐标名称
plt.yscale('log')                                       # 纵坐标为对数坐标
plt.legend(loc='best')                                  # 自动选择最佳图例位置
plt.title("Earn Money with Shannon's Strategy")         # 图表名称
plt.show()                                              # 显示图形
