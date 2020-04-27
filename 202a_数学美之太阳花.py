# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 调用自定义模块里的函数画太阳花

import turtle                           # 导入海龟作图函数库
from mylib.myflowers import *           # 导入自定义的画花函数库

tt = turtle.Turtle()                    # 产生一个海龟，名叫tt
sunflower(tt,"orange")                  # 调用自定义的画太阳花的函数
tt.hideturtle()                         # 隐藏海龟箭头

turtle.done()                           # 画画结束

