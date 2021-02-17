from tkinter import *
from tkinter import messagebox

import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if entry_website.get() == "" or entry_username.get() == "" or entry_password.get() == "":
        messagebox.showerror("Oops", "Please, don't leave any fields empty!")
    else:
        if messagebox.askokcancel("Confirm info", f"Website: {entry_website.get()}\n"
                                                  f"Email/Username: {entry_username.get()}\n"
                                                  f"Password: {entry_password.get()}\n\n"
                                                  f"Save?"):
            with open("data.txt", "a") as data:
                data.write(f"{entry_website.get()} | {entry_username.get()} | {entry_password.get()}\n")
            entry_password.delete(0, END)
            entry_website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Creating widgets
window = Tk()

button_add = Button(text="Add")
button_generatepass = Button(text="Generate Password")

canvas = Canvas(height=200, width=200)

entry_password = Entry(width=21)
entry_username = Entry(width=35)
entry_website = Entry(width=35)

label_password = Label(font=("Segoe UI", 10, "normal"), text="Password")
label_username = Label(font=("Segoe UI", 10, "normal"), text="Email/Username")
label_website = Label(font=("Segoe UI", 10, "normal"), text="Website")

# Configuring and placing widgets on the screen
logoimg = PhotoImage(file="logo.png")

window.config(padx=20, pady=20)
window.title("Password Manager")

canvas.create_image(100, 100, image=logoimg)
canvas.grid(column=1, row=0)

label_website.grid(column=0, row=1)

entry_website.grid(column=1, columnspan=2, row=1, sticky="EW")
entry_website.focus()

label_username.grid(column=0, row=2)

entry_username.grid(column=1, columnspan=2, row=2, sticky="EW")
entry_username.insert(0, "name@email.com")

label_password.grid(column=0, row=3)

entry_password.grid(column=1, row=3, sticky="EW")

button_generatepass.config(command=generatepassword)
button_generatepass.grid(column=2, row=3, sticky="EW")

button_add.config(command=save)
button_add.grid(column=1, columnspan=2, row=4, sticky="EW")

# Keeping window open
window.mainloop()
