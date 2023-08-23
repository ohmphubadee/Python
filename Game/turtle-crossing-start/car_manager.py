from turtle import Turtle
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
car_list = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.goto(x=300,y=random.randint(-260,280))
        self.setheading(180)
        self.speed = MOVE_INCREMENT
        car_list.append(self)

    def move(self):
        for car in car_list:
            car.forward(self.speed)

    def speedup(self):
        self.speed += 10