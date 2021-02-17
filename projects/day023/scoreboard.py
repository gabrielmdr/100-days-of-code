from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

        self.level = 1

        self.goto(-280, 260)
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Segoe UI", 14, "bold"))

    def update(self):
        self.clear()
        self.write(f"Level {self.level}", False, "left", ("Segoe UI", 14, "bold"))
