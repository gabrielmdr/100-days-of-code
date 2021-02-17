import random

from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_pos = (random.randint(-260, 260), random.randint(-260, 260))
        self.goto(random_pos)
