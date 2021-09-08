# # coding=utf-8
# import turtle
# import time
#
# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")
#
# turtle.tracer(False)
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
#     turtle.end_fill()
#
# turtle.mainloop()

# coding=utf-8
import turtle
import time

turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(2)

turtle.penup()
turtle.goto(-150, -120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))

turtle.mainloop()