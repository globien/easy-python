# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

import pandas as pd                 # 导入数据分析函数库
import matplotlib.pyplot as plt     # 导入图表函数库
import matplotlib.ticker as ticker  # 导入调整坐标表示的函数库

# 从文件读入数据，并筛选出其中两个国家/地区的数据
code1 = 'CHN'
code2 = 'USA'
data = pd.DataFrame(pd.read_csv('data/daily-cases-covid-19.csv'))
data1 = data.loc[data['Code'] == code1]
data2 = data.loc[data['Code'] == code2]

# 把上述删选的数据中相应的列分别拷贝到x轴和y轴，用于作图
x1 = data1['Date']   # 拷贝日期一列作为横坐标数据
x2 = data2['Date']   # 拷贝日期一列作为横坐标数据
y1 = data1['Daily confirmed cases (cases)']     # 拷贝每日确诊数作为纵坐标数据
y2 = data2['Daily confirmed cases (cases)']     # 拷贝每日确诊数作为纵坐标数据

# 创建画布和一个图表，大小为 12.8 x 4.8
fig, ax = plt.subplots(figsize = [12.8, 4.8])
ax.bar(x1, y1)  # 准备画第一组数据，以柱状图展示
ax.bar(x2, y2)  # 准备画第二组数据，以柱状图展示
plt.xlabel('Date')
plt.ylabel('Daily Confirmed Cases')

# 调节横坐标刻度，tick_spacing = 14 表示每过14天标一个横坐标标签
tick_spacing = 14
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

# 正式作图
plt.show()
