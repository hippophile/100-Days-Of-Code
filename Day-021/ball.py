from turtle import Turtle
from paddle import Paddle
import time
import random

class Ball(Turtle):
    y_col = False
    x_col = False
    p_col = False
    l_score = 0
    r_score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.seth(random.randint(0,360))
        self.speed("slowest")

    # make the move according to the collision
    def move(self):
        self.y_collision()
        if self.y_col:
            self.seth(-(self.heading()))
            self.forward(15)
            self.y_col = False

        self.x_collision()
        if self.x_col:
            self.reset()
            self.__init__()
            self.x_col = False

        time.sleep(0.05)
        self.forward(10)
        # print(f"{self.l_score}, {self.r_score}")

    # check collisions with y walls
    def y_collision(self):
        if self.ycor() > 380 or self.ycor() < -380:
            self.y_col = True
            return self.y_col

    # check collisions with walls and assign point
    def x_collision(self):
        if self.xcor() > 390:
            self.x_col = True
            self.l_score += 1
        elif self.xcor() < -390:
            self.x_col = True
            self.r_score += 1

            return self.x_col
        
    def r_paddle_col(self):
        self.seth(180-(self.heading()))
        self.forward(10)

    def l_paddle_col(self):
        self.seth(180-(self.heading()))
        self.forward(10)
        
