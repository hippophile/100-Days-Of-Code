from turtle import Turtle, Screen, colormode
from shapes import random_color
import random

def artsy():
    screen = Screen()
    t = Turtle()

    t.screen.title("MY ART")
    t.screen.bgcolor("black")

    t.shape("circle")
    t.pensize(2)
    t.speed(0)

    screen.setup(width=200, height=200, startx=0, starty=0)

    # for i in range(5):
        


    screen.exitonclick()