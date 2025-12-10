from turtle import Turtle, Screen, colormode
from shapes import random_color
import random

def walking(x):
    screen = Screen()
    t = Turtle()

    t.screen.title('Random Turtle Wlk')
    t.screen.bgcolor("black")

    t.shape("turtle")
    t.pensize(10)
    t.speed(10)

    for i in range(x):
        t.color(random_color())
        t.right(random.choice([0, 90, 180, -90]))
        t.forward(30)

    
    screen.exitonclick()
