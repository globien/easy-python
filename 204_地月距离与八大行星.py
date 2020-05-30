# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 计算和演示地月之间能否放下八大行星

import turtle

# 数据来源：https://www.wolframalpha.com/input/?i=planet+radius
planet_radius = {'Jupiter': 69950, 'Saturn': 58300, 'Uranus': 25360, 'Neptune': 24600, 'Earth': 6371, 'Venus': 6050, 'Mars': 3390, 'Mercury': 2440}
distance_earth_moon = {'Maximum': 405700, 'Average': 385000, 'Minimum': 363000}
moon_radius = 1737

print("八大行星直径总和：", sum(planet_radius.values()) * 2, '公里')
print("地月表面最大距离：", distance_earth_moon['Maximum']-planet_radius['Earth']-moon_radius, '公里')

ratio = 500                 # 把距离的公里数缩小为屏幕像素的比例，画图时使用

# 初始化Turtle
turtle.setup(1000, 600)
turtle.bgcolor("black")
tt = turtle.Turtle()
tt.penup()
tt.goto(-400, 0)
tt.pendown()

# 画地球
tt.pensize(1)
tt.setheading(90)
tt.pencolor('silver')
tt.fillcolor('RoyalBlue')
tt.begin_fill()
tt.circle(planet_radius['Earth'] / ratio)
tt.end_fill()

# 画月球
tt.setheading(0)
tt.pencolor('silver')
tt.fillcolor('silver')
tt.forward((distance_earth_moon['Maximum'] - planet_radius['Earth'] - moon_radius) / ratio)
tt.setheading(270)
tt.begin_fill()
tt.circle(moon_radius / ratio)
tt.end_fill()

# 在地球和月球之间画八大行星 —— 第一步，半圆画过去
tt.goto(-400, 0)
tt.pensize(2)
tt.setheading(90)
tt.pencolor('orange')
direction = 1
for planet in planet_radius:
    tt.write(planet, font=('Arial', int(planet_radius[planet] / ratio / 2), 'normal'))  # 打印行星名字
    direction *= -1
    tt.circle(planet_radius[planet] / ratio * direction, 180)

# 在地球和月球之间画八大行星 —— 第二步，半圆画回来
planet_radius = dict(sorted(planet_radius.items(), key=lambda x:x[1]))      # 按从小到大次序重新排列
direction = direction * -1
for planet in planet_radius:
    direction *= -1
    tt.circle(planet_radius[planet] / ratio * direction, 180)

turtle.done()
