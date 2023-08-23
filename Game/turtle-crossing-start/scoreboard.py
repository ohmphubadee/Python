from tkinter import font
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(x = -270,y = 250)
        self.write(f"Level: {self.level}",font=FONT)

    def game_over(self):
        self.ht()
        self.goto(0,0)
        self.write("GAME OVER",font=FONT,align='center')

    def count(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)