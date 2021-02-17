from tkinter import *

# Creating widgets
window = Tk()

entry_miles = Entry()

label_miles = Label(text="miles", font=("Segoe UI", 12, "normal"))
label_kms = Label(text="km", font=("Segoe UI", 12, "normal"))
label_isequalto = Label(text="is equal to", font=("Segoe UI", 12, "normal"))
label_kmsvalue = Label(text="0", font=("Segoe UI", 12, "normal"))

button_calculate = Button(text="Calculate")


# Creating calculation function
def calculate():
    miles = float(entry_miles.get())
    result = miles * 1.60934
    label_kmsvalue.config(text=result)


# Configuring and positioning widgets on the screen
window.configure(padx=50, pady=50)
window.title("Mile to Km Converter")

entry_miles.grid(column=1, row=0)
label_kmsvalue.grid(column=1, row=1)

label_miles.grid(column=2, row=0)
label_kms.grid(column=2, row=1)
label_isequalto.grid(column=0, row=1)

button_calculate["command"] = calculate
button_calculate.grid(column=1, row=2)

window.mainloop()
