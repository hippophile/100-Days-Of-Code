from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(position)
        self.color("white")
        
    def up(self):
        if self.ycor() < 330:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -320:
            self.goto(self.xcor(), self.ycor() - 20)