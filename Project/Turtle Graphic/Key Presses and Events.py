import turtle
import random
john = turtle.Turtle()

john.color('black')
john.pensize(10)
john.shape('circle')


def up():
    john.setheading(90)
    john.forward(30)


def down():
    john.setheading(270)
    john.forward(30)


def right():
    john.setheading(0)
    john.forward(30)


def left():
    john.setheading(180)
    john.forward(30)

def left_mouse_button(x, y):
    colors = ['red', 'yellow', 'orange', 'green', 'blue', 'black', 'pink']
    john.color(random.choice(colors))

def right_mouse_button(x, y):
    john.stamp()


turtle.listen()

turtle.onscreenclick(left_mouse_button, 1) # 1 là chuột trái, 2 là chính giữa, 3 là chuột phải
turtle.onscreenclick(right_mouse_button, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()

