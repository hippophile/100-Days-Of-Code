from turtle import Turtle 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake(3)
        self.head = self.all_segments[0]


    def create_snake(self, length,):

        for i in range(length):
            new_t = Turtle(shape="square")
            new_t.color("white")
            new_t.penup()
            new_t.goto(x=-20*i, y=0)
            self.all_segments.append(new_t)

    def move(self):
        for i in range(len(self.all_segments)-1, 0, -1):
            new_x = self.all_segments[i - 1].xcor() # 2nd to last tr
            new_y = self.all_segments[i - 1].ycor() # 2nd to last
            self.all_segments[i].goto(new_x, new_y)

        self.all_segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

