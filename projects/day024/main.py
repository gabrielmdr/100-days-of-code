names = []
startingletter = ""

# Open file and getting all names from it
with open("./Input/Names/invited_names.txt") as file:
    for line in file:
        names.append(line.strip())

# Getting the text from the starting letter
with open("./Input/Letters/starting_letter.txt") as file:
    startingletter = file.read()

# Looping through the list of names and writing the final version of the letter for each person
for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as readytosend:
        readytosend.write(startingletter.replace("[name]", name))
