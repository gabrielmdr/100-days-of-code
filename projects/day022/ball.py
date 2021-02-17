from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.movespeed = 0.1
        self.xmove = 10
        self.ymove = 10

        self.penup()

        self.color("white")
        self.shape("circle")

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def restart(self):
        self.goto(0, 0)
        self.movespeed = 0.1
        self.xbounce()
        self.ymove = 10

    def xbounce(self):
        self.movespeed *= 0.9
        self.xmove *= -1

    def ybounce(self):
        self.movespeed *= 0.9
        self.ymove *= -1
