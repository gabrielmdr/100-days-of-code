from art import logo, vs
from game_data import data

import random

game_over = False
score = 0

b = random.choice(data)

while not game_over:
    print(logo)

    a = b
    b = random.choice(data)
    while b["name"] == a["name"]:
        b = random.choice(data)

    if score > 0:
        print(f"You're right. Current score: {score}.")

    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}.")

    guess = input("Who has more followers. Type 'A' or 'B': ").lower()

    if a["follower_count"] > b["follower_count"]:
        if guess != "a":
            game_over = True
    elif b["follower_count"] > a["follower_count"]:
        if guess != "b":
            game_over = True

    if not game_over:
        score += 1

print(f"Sorry, that's wrong. Final score: {score}.")
