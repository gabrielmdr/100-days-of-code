from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

currentword = {}
facingfront = True
fliptimer = None

# Reading the word file
try:
    worddf = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    worddf = pandas.read_csv("./data/french_words.csv")

# Creating the word list
wordlist = [{
    "French": row["French"],
    "English": row["English"]
} for (index, row) in worddf.iterrows()]

# Creating window
window = Tk()

# Images
cardback_img = PhotoImage(file="images/card_back.png")
cardfront_img = PhotoImage(file="images/card_front.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Creating widgets
canvas = Canvas(bg=BACKGROUND_COLOR, height=526, highlightthickness=0, width=800)
right_button = Button(highlightthickness=0, image=right_img)
wrong_button = Button(highlightthickness=0, image=wrong_img)


# Functions
def drawword():
    global currentword

    currentword = random.choice(wordlist)


def flip(right):
    global fliptimer

    if fliptimer:
        window.after_cancel(fliptimer)

    if right:
        wordlist.remove(currentword)
        newworddf = pandas.DataFrame(wordlist)
        newworddf.to_csv("./data/words_to_learn.csv", index=False)

    drawword()
    flipfront()


def flipback():
    canvas.itemconfig(canvasimg, image=cardback_img)
    canvas.itemconfig(languagetxt, fill="white", text="English")
    canvas.itemconfig(wordtxt, fill="white", text=currentword["English"])


def flipfront():
    global fliptimer

    canvas.itemconfig(canvasimg, image=cardfront_img)
    canvas.itemconfig(languagetxt, fill="black", text="French")
    canvas.itemconfig(wordtxt, fill="black", text=currentword["French"])
    fliptimer = window.after(3000, flipback)


def rightbutton_click():
    flip(True)


def wrongbutton_click():
    flip(False)


# Setting up widgets
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

canvasimg = canvas.create_image(400, 263, image=cardfront_img)
languagetxt = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="Title")
wordtxt = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="Word")

right_button.config(command=rightbutton_click)
wrong_button.config(command=wrongbutton_click)

drawword()
flipfront()

# Placing widgets on the window
canvas.grid(column=0, columnspan=2, row=0)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

# Keeping the window open
window.mainloop()
