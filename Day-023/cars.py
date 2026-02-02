from turtle import Turtle
from randcolor import random_color
import time

class Car(Turtle):
    speeds = 5

    def __init__(self, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.right(180)
        self.shapesize(1, 3)
        self.goto(400, y)
        self.color(random_color())
        self.speed(0.1)

    def move(self):
        self.forward(self.speeds)
    