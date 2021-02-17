from tkinter import *

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timertext, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_completed.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    if reps == 8:
        label_timer.config(text="Break", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    else:
        label_timer.config(text="Work", fg=GREEN)
        countdown(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(timeamount):
    minutes = math.floor(timeamount / 60)
    seconds = timeamount % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timertext, text=f"{minutes}:{seconds}")
    if timeamount > 0:
        global timer
        timer = window.after(1000, countdown, timeamount - 1)
    else:
        start()
        checkmarks = ""
        for _ in range(math.floor(reps / 2)):
            checkmarks += "✔"
        label_completed.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #

# Creating widgets
window = Tk()

button_start = Button(text="Start")
button_reset = Button(text="Reset")

canvas = Canvas(bg=YELLOW, width=200, height=224, highlightthickness=0)

label_timer = Label(text="Timer", font=("Segoe UI", 36, "bold"))
label_completed = Label(font=("Segoe UI", 14, "bold"))

tomatoimg = PhotoImage(file="tomato.png")


# Configuring and placing widgets on the screen
window.config(bg=YELLOW, padx=100, pady=50)
window.title("Pomodoro")

label_timer.config(bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)
label_completed.config(bg=YELLOW, fg=GREEN)
label_completed.grid(column=1, row=3)

canvas.create_image(100, 112, image=tomatoimg)
timertext = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start.config(command=start)
button_start.grid(column=0, row=2)
button_reset.config(command=reset)
button_reset.grid(column=2, row=2)

# Keeping window open
window.mainloop()
