import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if choice == 0:
    print(symbols[choice])
    if computer_choice == 0:
        result = "It\'s a draw."
    elif computer_choice == 1:
        result = "You lose."
    else:
        result = "You win!"
elif choice == 1:
    print(symbols[choice])
    if computer_choice == 0:
        result = "You win!"
    elif computer_choice == 1:
        result = "It\'s a draw."
    else:
        result = "You lose."
elif choice == 2:
    print(symbols[choice])
    if computer_choice == 0:
        result = "You win!"
    elif computer_choice == 1:
        result = "You lose."
    else:
        result = "It\'s a draw."
else:
    result = "You typed an invalid number. You lose."

print("Computer chose:")
print(symbols[computer_choice])
print(result)
