import pandas
import turtle

guessed = []
states = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

isgameon = True

while len(guessed) < 50:
    guess = screen.textinput(f"{len(guessed)}/50 Guessed", "What's another state name? (Type 'Exit' to exit)").title()
    if guess == "Exit":
        statenames = states["state"].to_list()
        missingstates = []

        for statename in statenames:
            if statename not in guessed:
                missingstates.append(statename)

        missingstatesdf = pandas.DataFrame(missingstates)
        missingstatesdf.to_csv("states_to_learn.csv")
        break
    if guess in states["state"].to_list():
        guessed.append(guess)
        state = states[states["state"] == guess]
        writer.goto(int(state["x"]), int(state["y"]))
        writer.write(guess, False, "center", ("Segoe UI", 8, "normal"))
