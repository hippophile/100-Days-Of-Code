from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

# classes

player = Player()
all_cars = []
counter = 0
scoreboard = Scoreboard()

# screen
screen.listen()
screen.onkey(player.move, "Up")
score = 0

# game loop
spawn_rate = 10
game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.05)
    scoreboard.refresh_score(score)
    counter += 1


    if counter >= spawn_rate:
        new_car = Car(random.randint(-390, 350))
        all_cars.append(new_car)
        counter = 0

    for car in all_cars:
        car.move()

        if car.xcor() < -390:
            car.ht()
            all_cars.remove(car)

        if car.distance(player) < 15:
            
            scoreboard.game_over(score)
            print(f"Game over at score : {score}")
            screen.update()
            game_is_on = False
        

    if player.ycor() > 395:
        score += 1
        print(f"Score is {score} ")
        player.goto(0, -370)
        # spawn_rate -= 1 # THIS IS FOR MAKING MORE CARS
        car.speeds += 2   # THSI IS FOR MAKING THE CARS FASTER
    
screen.exitonclick()