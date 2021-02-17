from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        
        self.color("white")
        self.goto(x, y)
        self.turtlesize(5, 1)
        self.shape("square")
        self.shapesize(5, 1)

    def moveup(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def movedown(self):
        self.goto(self.xcor(), self.ycor() - 20)
