import turtle
import random
import math

# 定义圣诞树的绿叶函数
def tree(d, s):
    if d <= 0:
        return

    turtle.forward(s)
    tree(d - 1, s * .7)
    turtle.right(120)
    tree(d - 2.6, s * .5)
    turtle.right(120)
    tree(d - 2.6, s * .5)
    turtle.right(120)
    turtle.backward(s)


n = 100
""" 设置绘图速度
'fastest' : 0
'fast'  : 10
'normal' : 6
'slow'  : 3
'slowest' : 1
"""
turtle.pensize(2)
turtle.bgcolor("black")
turtle.hideturtle()
turtle.speed(0) # 设置速度
turtle.left(90)
turtle.forward(2 * n)
turtle.color("yellow")
turtle.left(126)

turtle.begin_fill()
for i in range(5):
    turtle.forward(n / 8)
    turtle.right(144)
    turtle.forward(n / 8)
    turtle.left(72)
turtle.fillcolor("yellow")
turtle.end_fill()

turtle.right(126)
turtle.color("dark green")
turtle.backward(n * 3.2)

# 执行函数
tree(10, n)
turtle.backward(n / 5)

turtle.color("orange")
turtle.write("Merry Christmas",align="center",font=("Brush Script MT",40))

x=[5,  10, -24, 30, 24,-27,-45,38,-6,12,29,-15,8,75,-38,-17,56,69 ,-74,-9, 67,-36]
y=[160,146,136,122,108,100,89, 78,67,55,38,24,16,3,-19,-36,-22,-34,-46,-55,-61,-66]
xr=x[0:21:2]
yr=y[0:21:2]
xy=x[1:22:2]
yy=y[1:22:2]
for i in range(0,10):
    turtle.penup()
    turtle.goto(xy[i],yy[i])
    turtle.color("yellow")
    turtle.dot(5)
for i in range(0,10):
    turtle.penup()
    turtle.goto(xr[i],yr[i])
    turtle.color("red")
    turtle.dot(5)
turtle.penup()
turtle.goto(34,-66)
turtle.color("red")
turtle.dot(5)

turtle.penup()
turtle.goto(-290,200)
turtle.color("yellow")
turtle.write("author:YIMINGLI",font=("Baskerville Old Face",16))

turtle.penup()
turtle.goto(69,-160)
turtle.color("yellow")
turtle.write("To sameone",font=("楷体",20))

turtle.done()

