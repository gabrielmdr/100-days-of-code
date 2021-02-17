from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

import time

screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

p1 = Paddle(350, 0)
p2 = Paddle(-350, 0)

ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(p1.moveup, "Up")
screen.onkey(p1.movedown, "Down")
screen.onkey(p2.moveup, "w")
screen.onkey(p2.movedown, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.movespeed)

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.ybounce()

    if (ball.distance(p1) < 50 and ball.xcor() > 320) or (ball.distance(p2) < 50 and ball.xcor() < -320):
        ball.xbounce()

    if ball.xcor() >= 390:
        scoreboard.lpoint()
        ball.restart()

    if ball.xcor() <= -390:
        scoreboard.rpoint()
        ball.restart()

    ball.move()
    screen.update()

screen.exitonclick()
