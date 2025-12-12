# if you dont think that this here is not art guess what?
# Many painting just like this were sold from a few hundreds thousand to a few millions dollars

from turtle import Turtle, Screen, colormode
from shapes import random_color
import random

def artsy(x, y):
    screen = Screen()
    t = Turtle()

    t.screen.title('MY ART')
    t.screen.bgcolor("black")

    fo = 115
    up = 200
    t.shape("turtle")
    t.pensize(0)
    t.speed(0)

    screen.setup(width=.99, height=.99, startx=0, starty=0)
    t.teleport(-350, -300)

    t.ht()

    left = True
    right = False
    for i in range(x):
        if i % 2 != 0 :
            left = False
            right = True
        elif i % 2 == 0:
            left = True
            right = False
        for j in range(y):

            t.color(random_color())
            t.begin_fill()
            t.circle(30)
            t.end_fill()

            if j != y-1:
                t.penup()
                t.forward(fo)
                t.pendown()
    
            if j == y-1 and right:
                t.penup()
                t.right(90)
                t.forward(up/2)
                t.right(90)
                t.pendown()
                # left = True
                # right = False

            if j == y-1 and left:
                t.penup()
                t.left(90)
                t.forward(up)
                t.left(90)
                t.pendown()
                # left = False
                # right = True

            
    t.color("black")

    screen.exitonclick()