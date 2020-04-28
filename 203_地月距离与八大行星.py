# 作者：西岛闲鱼
# https://github.com/globien/easy-python
# https://gitee.com/globien/easy-python

# 计算和演示地月之间能否放下八大行星

import turtle
import collections

# 数据来源：https://www.wolframalpha.com/input/?i=planet+radius
planet_radius = collections.OrderedDict()
planet_radius = {'Jupiter': 69950, 'Saturn': 58300, 'Uranus': 25360, 'Neptune': 24600, 'Earth': 6371,
                 'Venus': 6050, 'Mars': 3390, 'Mercury': 2440, 'Moon': 1737}
moon_radius = 1737
distance_earth_moon = {'Maximum': 405700, 'Average': 385000, 'Minimum': 363000}

print("Sum of all planet radius:", sum(planet_radius.values()) * 2)
print("Maximum distance from Earth to Moon:", distance_earth_moon['Maximum'])

ratio = 500

turtle.setup(1000, 600)
turtle.bgcolor("black")

tt = turtle.Turtle()
tt.penup()
tt.goto(-400, 0)
tt.pendown()

tt.pensize(1)
tt.setheading(90)
tt.pencolor('silver')
tt.fillcolor('blue')
tt.begin_fill()
tt.circle(planet_radius['Earth'] / ratio)
tt.end_fill()

tt.setheading(0)
tt.pencolor('silver')
tt.fillcolor('silver')
tt.forward((distance_earth_moon['Maximum'] - planet_radius['Earth'] - moon_radius) / ratio)
tt.setheading(270)
tt.begin_fill()
tt.circle(moon_radius / ratio)
tt.end_fill()

tt.goto(-400, 0)
tt.pensize(2)
tt.setheading(90)
tt.pencolor('orange')
direction = 1
for planet in planet_radius:
    tt.write(planet, font=('Arial', int(planet_radius[planet] / ratio / 2), 'normal'))
    direction *= -1
    tt.circle(planet_radius[planet] / ratio * direction, 180)

planet_radius = collections.OrderedDict(reversed(list(planet_radius.items())))
direction = direction * -1
for planet in planet_radius:
    direction *= -1
    tt.circle(planet_radius[planet] / ratio * direction, 180)

turtle.done()
