import numpy as np
from matplotlib import pyplot as plt
num_cases = [115, 142, 198, 235, 343, 436, 596, 727, 873, 1087, 1330, 1470, 2091, 2792]   # number of cases in order of dates

days = len(num_cases)                  # count the days input with the number of cases
x = [ i+1 for i in range(days) ]         # x coordinate, in days
y = num_cases                             # y coordinate, i.e., number of cases for each day
plt.scatter(x, y)                             # print the original numbers in dots

# simulate with polynomial of degree 3
parameters = np.polyfit(x, y, 3)
func = np.poly1d(parameters)

# predict for more days
days_extended = 14                          
for i in range(days_extended):                  
    x.append(days+i+1)              
plt.plot(x, func(x), color='g')
plt.xlabel('days')
plt.ylabel('number of cases')
plt.title('A rough prediction of the number of cases by simulation')
plt.show()
