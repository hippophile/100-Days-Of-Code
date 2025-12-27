from turtle import Turtle 
from scoreboard import Scoreboard

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
COLOR = "white"
SNAKE_LEN = 3

class Snake():
    

    def __init__(self):
        self.snake_len = SNAKE_LEN
        self.all_segments = []
        self.create_snake(self.snake_len)
        self.head = self.all_segments[0]
        self.tail = self.all_segments[self.snake_len-1]
        self.player_lost = False


    def create_snake(self, length):

        for i in range(length):
            new_t = Turtle(SHAPE)
            new_t.color(COLOR)
            new_t.penup()
            new_t.goto(x=-20*i, y=0)
            self.all_segments.append(new_t)
        
    # extend always by 1 
    def extend(self):
        new_t = Turtle(SHAPE)
        new_t.color(COLOR)
        new_t.penup()
        last_x = self.tail.xcor()
        last_y = self.tail.ycor()
        new_t.goto(last_x, last_y-10)
        self.snake_len += 1
        self.all_segments.append(new_t)

    def move(self):
        for i in range(len(self.all_segments)-1, 0, -1):
            new_x = self.all_segments[i - 1].xcor() # 2nd to last tr
            new_y = self.all_segments[i - 1].ycor() # 2nd to last
            self.all_segments[i].goto(new_x, new_y)

        self.all_segments[0].forward(20)
        
    def check_game(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.player_lost = True
        for th in self.all_segments:
            if th == self.head:
                pass
            elif self.head.distance(th) < 10:
                self.player_lost = True


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