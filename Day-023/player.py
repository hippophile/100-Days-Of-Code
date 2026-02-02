from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(1, 1)
        self.color("green")
        self.speed("fastest")
        self.left(90)
        self.goto(0, -370)

    def move(self):
        self.forward(20)