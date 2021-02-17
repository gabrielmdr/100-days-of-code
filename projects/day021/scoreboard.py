from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Segoe UI", 12, "normal"))

    def increment(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score {self.score}", False, "center", ("Segoe UI", 12, "normal"))
