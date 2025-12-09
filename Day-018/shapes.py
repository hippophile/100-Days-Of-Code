from turtle import Turtle, Screen, colormode
import random

colormode(255)

t = Turtle()
t.shape("circle")
t.pensize(2)
t.speed(0)

t.penup()
t.goto(0, 300)
t.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range (3,361):
    t.color(random_color())
    for _ in range(i):
        t.right(360/i)
        t.forward(100)


screen = Screen()
screen.exitonclick()
