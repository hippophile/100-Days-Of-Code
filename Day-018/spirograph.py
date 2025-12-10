from turtle import Turtle, Screen, colormode
from shapes import random_color
import random

def spiro(size):

    screen = Screen()
    t = Turtle()

    t.screen.title('Spirography')
    t.screen.bgcolor("black")

    t.shape("classic")
    # t.pensize()
    t.speed(0)

    for i in range(int(360/size)):
        t.color(random_color())
        t.circle(100)
        t.left(size)



    screen.exitonclick()