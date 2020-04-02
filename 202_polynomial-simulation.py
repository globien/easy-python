# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python
# 多项式曲线拟合

import numpy as np
from matplotlib import pyplot as plt

# number of cases in order of dates
num_cases = [115, 142, 198, 235, 343, 436, 596, 727, 873, 1087, 1330, 1470, 2091, 2792]

days = len(num_cases)                  # count the days input with the number of cases
x = [ i+1 for i in range(days) ]       # x coordinate, in days
y = num_cases                          # y coordinate, i.e., number of cases for each day
plt.scatter(x, y)                      # print the original numbers in dots

# simulate with polynomial of degree 3
parameters = np.polyfit(x, y, 3)
func = np.poly1d(parameters)

# extend for more days and draw the curve
days_extend = 14                          
for i in range(days_extend):
  x.append(days+i+1)
plt.plot(x, func(x), color='g')
plt.xlabel('days')
plt.ylabel('number of cases')
plt.title('A Rough Prediction of the Number of Cases by Simulation')
plt.show()
