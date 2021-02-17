from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.goto(0, -280)
        self.setheading(90)
        self.shape("turtle")

    def gotostart(self):
        self.goto(0, -280)

    def isatfinish(self):
        if self.ycor() >= 290:
            return True
        else:
            return False

    def move(self):
        self.forward(10)
