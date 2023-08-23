from tkinter import CENTER
from turtle import write, clear,Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        self.write(f'Score :  {self.score}',False,align='center',font=(8))
        self.ht()

    def count(self):
        self.score += 1
        self.clear()
        self.write(f'Score :  {self.score}',False,align='center',font=(8))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=8)
