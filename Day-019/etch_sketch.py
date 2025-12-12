from turtle import Turtle, Screen, colormode
import random

t = Turtle()

def move_forwards():
    t.forward(10)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def backwards():
    t.backward(10)

def restart():
    t.reset()

def sketch():
    screen = Screen()
    

    t.screen.title('Random Turtle Walk')
    t.screen.bgcolor("white")

    t.shape("arrow")


    screen.listen()

    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=backwards)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)

    screen.onkey(key="c", fun=restart)



    screen.exitonclick()

sketch()