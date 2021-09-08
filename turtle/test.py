# 彩色螺旋线
# coding=utf-8

import turtle

import time
turtle.pensize(2)
turtle.bgcolor("black")
# colors = ["red","yellow","purple","blue","yellow","purple","blue","purple","blue","blue"]
colors = ["red", "yellow", "purple", "blue"]

# turtle.tracer(True)
turtle.tracer(False)
turtle.speed(0)
for x in range(180):
    # turtle.forward(2 * x)  # 向当前画笔方向移动distance像素长度
    # turtle.left(91)  # 逆时针移动degree°
    # turtle.forward(2 * x)  # 向当前画笔方向移动distance像素长度
    # turtle.right(-91)  # 顺时针移动degree°
    # turtle.circle(5*x)
    # turtle.dot(x)# 绘制一个指定直径和颜色的圆点
    # turtle.backward(1 * x)
    # turtle.goto(x, 10*x)  # 将画笔移动到坐标为x, y的位置
    turtle.circle(50, steps=3)  # 三角形;
    turtle.color(colors[x % 4])
# turtle.update()
turtle.done()

