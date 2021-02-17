from turtle import Turtle, Screen

import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

turtles = []
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n"
                                                          f"{colors}")

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-240, y=75 - 30 * i)
    turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if is_race_on and turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

            is_race_on = False

screen.exitonclick()
