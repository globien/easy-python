#割圆法，设圆半径r=1，内接n边形边长a[n]=sqrt(2-2*sqrt(1-(a[n/2]/2)**2))，则pi=n*a[n]/2
#初始从内接正六边形开始，a[6]=r=1

import math

print("将进行无限计算，请用Ctrl_C或其他方式强制退出！！！")
input("按回车(Enter)键开始...")
print("开始计算...，退出请用Ctrl_C或其他强制退出方式...")
print("\n实验次数        计算结果")

n=6
a=1
print(n,"     ",n*a/2)
for i in range(100) :
  n=2*n
  a=math.sqrt(2-2*math.sqrt(1-(a/2)**2))
  print(n,"     ",n*a/2)
