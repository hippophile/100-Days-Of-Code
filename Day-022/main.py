from turtle import Screen
from player import Player

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

# classes

player = Player()



screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()