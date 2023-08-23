from email.contentmanager import raw_data_manager
from re import S
import time
import turtle
from paddle import Paddle
from ball import Ball
from turtle import Screen, Turtle, xcor
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('My pong game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
r_scoreboard = Scoreboard((200,280))
l_scoreboard = Scoreboard((-200,280))

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        if ball.ball_speed > 0.01:
            ball.ball_speed -= 0.01
    if ball.xcor() == 390:
        ball.reset_position()
        l_scoreboard.count()
        ball.ball_speed = 0.1

    if ball.xcor() == -390:
        ball.reset_position()
        r_scoreboard.count()
        ball.ball_speed = 0.1
    


    
        
        


screen.exitonclick()