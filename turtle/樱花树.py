# encoding:utf-8
import turtle
import random
from math import *


class Tree:
    def __init__(self):
        # turtle.setup(1000, 700)
        turtle.bgcolor(1, 1, 1)  # 背景色
        # ht()  # 隐藏turtle
        turtle.speed(0)  # 速度 1-10渐进，0 最快
        # tracer(1, 100)    # 设置绘图屏幕刷新频率，参数1设置在正常刷新频次的第参数1次刷新，参数2设置每次刷新的时延
        # turtle.tracer(0, 0)
        turtle.pu()  # 抬笔
        turtle.backward(100)
        # 保证笔触箭头方向始终不向下，此处使其左转90度，而不是右转
        turtle.left(90)  # 左转90度
        turtle.backward(300)  # 后退300

    def tree(self, n, l):
        turtle.pd()  # 下笔
        # 阴影效果
        t = cos(radians(turtle.heading() + 45)) / 8 + 0.25
        turtle.pencolor(t, t, t)
        turtle.pensize(n / 1.2)
        turtle.forward(l)  # 画树枝
        if n > 0:
            b = random.random() * 15 + 10  # 右分支偏转角度
            c = random.random() * 15 + 10  # 左分支偏转角度
            d = l * (random.random() * 0.25 + 0.7)  # 下一个分支的长度
            # 右转一定角度,画右分支
            turtle.right(b)
            self.tree(n - 1, d)
            # 左转一定角度，画左分支
            turtle.left(b + c)
            self.tree(n - 1, d)
            # 转回来
            turtle.right(c)
        else:
            # 画叶子
            turtle.right(90)
            n = cos(radians(turtle.heading() - 45)) / 4 + 0.5
            turtle.pencolor(n, n * 0.8, n * 0.8)
            turtle.fillcolor(n, n * 0.8, n * 0.8)
            turtle.begin_fill()
            turtle.circle(3)
            turtle.left(90)
            turtle.end_fill()
            # 添加0.3倍的飘落叶子
            if random.random() > 0.7:
                turtle.pu()
                # 飘落
                t = turtle.heading()
                an = -40 + random.random() * 40
                turtle.setheading(an)
                dis = int(800 * random.random() * 0.5 + 400 * random.random() * 0.3 + 200 * random.random() * 0.2)
                turtle.forward(dis)
                turtle.setheading(t)
                # 画叶子
                turtle.pd()
                turtle.right(90)
                n = cos(radians(turtle.heading() - 45)) / 4 + 0.5
                turtle.pencolor(n * 0.5 + 0.5, 0.4 + n * 0.4, 0.4 + n * 0.4)
                turtle.fillcolor(n, n * 0.8, n * 0.8)
                turtle.begin_fill()
                turtle.circle(2)
                turtle.left(90)
                turtle.end_fill()
                turtle.pu()
                # 返回
                t = turtle.heading()
                turtle.setheading(an)
                turtle.backward(dis)
                turtle.setheading(t)
                # pass
        turtle.pu()
        turtle.backward(l)  # 退回


def main():
    tree = Tree()
    tree.tree(12, 100)  # 递归7层
    turtle.done()


if __name__ == '__main__':
    main()
