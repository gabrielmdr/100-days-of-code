from turtle import Turtle

import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.color(random.choice(colors))
        self.goto(320, random.randint(-250, 250))
        self.setheading(180)
        self.shape("square")
        self.shapesize(1, 2)
        self.turtlesize(1, 2)

    def move(self, movespeed):
        self.forward(movespeed)
