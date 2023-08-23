from turtle import Turtle
from turtle import Turtle 


class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color('white')
        self.goto(position)
        self.write(f'{self.score}',font=80)

    def count(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}',font =80)
        