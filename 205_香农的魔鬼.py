from random import randint
import matplotlib.pyplot as plt

days = 300                  # 总共投资多少天
cash = 1.0                  # 初始现金

print("\n多次实验，每次实验最终（第300天）的股价与总资产对比：\n")
for i in range(20):
    money = value = cash / 2    # 一半买为股票，一般保留现金
    price = 1.0                 # 初始股票价格
    shares = value / price      # 初始买的股票数，假定允许买卖分数股数

    moneys = [money]
    values = [value]
    prices = [price]
    assets = [money + value]


    for day in range(1, days):
        price = price * 2**(randint(0,1)*2-1)
        prices.append(price)
        temp_value = shares * price
        delta = (temp_value - money) / price / 2  # 准备卖出（或买入）股值与现金差值的一半对应股票，以保持股值与现金相等
        shares = shares - delta
        value = shares * price
        values.append(value)
        money = money + delta * price
        moneys.append(money)
        assets.append(money + value)
    print("第{:2d}次实验结果： Price = {:.2e}   Assets = {:.2e}".format(i+1, prices[days-1],assets[days-1]))

print()
print()
for day in range(days):
    print("day {}   Price = {:.2e}   Assets = {:.2e} ".format(day+1, prices[day], assets[day]))

plt.plot(range(days), prices, label='Stock Price')
plt.plot(range(days), assets, label='Total Assets')
plt.xlabel('Days', )
plt.ylabel('Total Assets / Stock Price')
plt.yscale('log')
plt.legend(loc='best')
plt.title("Earn Money with Shannon's Strategy")
plt.show()
