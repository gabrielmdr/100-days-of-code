from turtle import Screen

from car import Car
from player import Player
from scoreboard import Scoreboard

import time

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)

cars = []
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

generatecar = 1
isgameon = True
movespeed = 5

while isgameon:
    time.sleep(0.1)
    for car in cars:
        car.move(movespeed)
        if car.distance(player) < 20:
            scoreboard.gameover()
            isgameon = False
    if generatecar % 6 == 0:
        cars.append(Car())
    if player.isatfinish():
        scoreboard.level += 1
        movespeed += 2.5
        player.gotostart()
        scoreboard.update()
    screen.update()
    generatecar += 1

screen.exitonclick()
