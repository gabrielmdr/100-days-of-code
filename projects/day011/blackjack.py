from art import logo

import random


def compare(opponent_score, user_score):
    if user_score > 21 and opponent_score > 21:
        return "You went over. You lose."
    elif user_score == opponent_score:
        return "It's a draw."
    elif opponent_score == 0:
        return "Opponent has a Blackjack. You lose."
    elif user_score == 0:
        return "You have a Blackjack. You win."
    elif user_score > 21:
        return "You went over. You lose."
    elif opponent_score > 21:
        return "Opponent went over. You win."
    elif user_score > opponent_score:
        return "You win."
    else:
        return "You lose."


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


av_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play = True
else:
    play = False

while play:
    print(logo)

    player_cards = [random.choice(av_cards)]

    dealer_cards = [random.choice(av_cards), random.choice(av_cards)]

    player_score = 0

    dealer_score = calculate_score(dealer_cards)

    hit = True

    while hit:
        player_cards.append(random.choice(av_cards))

        player_score = calculate_score(player_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_score < 21 and player_score != 0:
            if input("Type 'y' to get another card, type 'n' to pass: ") != "y":
                hit = False
        else:
            hit = False

    while dealer_score < 17:
        dealer_cards.append(random.choice(av_cards))
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    print(compare(dealer_score, player_score))

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != "y":
        play = False
