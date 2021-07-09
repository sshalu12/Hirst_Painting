# import colorgram

# colors = colorgram.extract('hirst-1.jpg', 30)
# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)

import random
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)

t1 = Turtle()
colors = [(194, 160, 120), (72, 92, 125), (143, 87, 59), (216, 209, 122),
          (140, 160, 188), (183, 147, 162), (29, 33, 46), (119, 73, 92), (56, 35, 26), (174, 160, 42), (139, 174, 153), (78, 115, 80), (62, 30, 40)]


t1.speed("fastest")
t1.penup()
t1.hideturtle()
t1.setheading(225)
t1.forward(300)
t1.setheading(0)
for i in range(1, 101):
    t1.dot(15, random.choice(colors))
    t1.forward(50)
    if i % 10 == 0:
        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)
        t1.setheading(0)


s = Screen()
s.exitonclick()
