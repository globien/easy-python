#割圆法，设圆半径r=1，内接n边形边长a[n]=sqrt(2-2*sqrt(1-(a[n/2]/2)**2))，则pi=n*a[n]/2
#初始从内接正六边形开始，a[6]=r=1
#因为计算机精度原因，64位机算到49512边形就无法继续提高计算结果的精度了

import math

n=6
a=1
print(n,"     ",n*a/2)
for i in range(15) :
  n=2*n
  a=math.sqrt(2-2*math.sqrt(1-(a/2)**2))
  print(n,"     ",n*a/2)
