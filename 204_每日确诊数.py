import pandas as pd  # 数据分析
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 读入数据，并筛选出中国和美国的数据
data = pd.DataFrame(pd.read_csv("data/daily-cases-covid-19.csv"))
data_CHN = data.loc[data["Code"] == "CHN"]
data_USA = data.loc[data["Code"] == "USA"]

x = data_CHN['Date']
y1 = data_CHN['Daily confirmed cases (cases)']
y2 = data_USA['Daily confirmed cases (cases)']
tick_spacing = 14                       # 此数据用于调节横坐标密度

fig, ax = plt.subplots(1,1)
ax.bar(x,y1)
ax.bar(x,y2)
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
plt.show()
