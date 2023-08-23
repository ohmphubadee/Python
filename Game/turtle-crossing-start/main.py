from random import randint
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager, car_list
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car = CarManager()
cars = car_list

screen.listen()
screen.onkey(player.goup,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if randint(0,1) == 1:
        car = CarManager()
    car.move()
    for car in cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() == 280:
        player.reset()
        scoreboard.count()
        car.speedup()

screen.exitonclick()
