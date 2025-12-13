from turtle import Turtle 

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake(3)
        


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
        self.all_segments[0].rt(90)


# def forwards(t):
#     t.seth(0)
#     t.forward(10)

# def left(t):
#     t.seth(270)
#     t.forward(10)

# def right(t):
#     t.seth(90)
#     t.forward(10)

# def down():
#     Turtle.setheading(180)
#     Turtle.forward(10)


# screen.onkey(key="w", fun=forwards)
# screen.onkey(key="s", fun=down)
# screen.onkey(key="a", fun=left)
# screen.onkey(key="d", fun=right)