import random
from turtle import Screen, Turtle

colors_list = [
    (145, 28, 64),
    (239, 75, 35),
    (6, 148, 93),
    (232, 238, 234),
    (231, 168, 40),
    (184, 158, 46),
    (44, 191, 233),
    (27, 127, 195),
    (126, 193, 74),
    (253, 223, 0),
    (85, 28, 93),
    (173, 36, 97),
    (246, 219, 44),
    (44, 172, 112),
    (215, 130, 165),
    (215, 56, 27),
    (235, 164, 191),
    (156, 24, 23),
    (21, 188, 230),
    (238, 169, 157),
    (162, 210, 182),
    (138, 210, 232),
    (0, 123, 54),
    (88, 130, 182),
    (180, 187, 211)
]

turtle = Turtle()

screen = Screen()
screen.colormode(255)

turtle.hideturtle()
turtle.speed("fastest")

turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(270)
turtle.right(180)

for _ in range(10):
    print(f"{turtle.xcor()}, {turtle.ycor()}")
    for _ in range(10):
        turtle.dot(20, random.choice(colors_list))
        turtle.forward(50)
    turtle.right(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)

screen.exitonclick()
