from turtle import Turtle, Screen, colormode
import random

colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def shaping(x):

    t = Turtle()

    t.shape("arrow")
    t.pensize(2)
    t.speed(0)

    t.penup()
    t.goto(0, 300)
    t.pendown()

    for i in range (3,x):
        t.color(random_color())
        for _ in range(i):
            t.right(360/i)
            t.forward(100)

    screen = Screen()
    screen.exitonclick()
