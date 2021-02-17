from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.lscore = 0
        self.rscore = 0

        self.color("white")
        self.hideturtle()

        self.update()

    def lpoint(self):
        self.lscore += 1
        self.update()

    def rpoint(self):
        self.rscore += 1
        self.update()

    def update(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.lscore, False, "center", ("Courier", 60, "bold"))

        self.goto(100, 200)
        self.write(self.rscore, False, "center", ("Courier", 60, "bold"))
