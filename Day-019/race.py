from turtle import Turtle, Screen, colormode
import random

NAMED_COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

def race():
    t = Turtle()
    t.hideturtle()

    race = True

    turtles = 5
    screen = Screen()
    screen.setup(width=500, height=400)
    # user_bet = screen.textinput(title="Make your bet", prompt="Which turtke will win the race? Enter a color: ")
    # print(user_bet)
    all_ts = []

    for i in range(turtles):
        new_t = Turtle(shape="turtle")
        new_t.color((NAMED_COLORS[i]))
        new_t.penup()
        new_t.goto(x=-230, y=-100+i*50)
        all_ts.append(new_t)

    while race:
        for t in all_ts:
            rand_dist = random.randint(0,10)
            t.forward(rand_dist)
            if t.xcor() > 230:
                race = False
                print(t.pencolor())

    screen.exitonclick()

race()