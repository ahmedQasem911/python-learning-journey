# Card Drawing Program
# --------------------
# A simple command-line program that simulates drawing cards from a shuffled deck.
#
# How it works:
#     1. Creates a standard 52-card deck and shuffles it.
#     2. Asks the user how many cards to draw (0 to quit).
#     3. Validates the input (not a number, negative, or more than the remaining cards).
#     4. Draws the cards from the deck and displays each one as ASCII art.
#     5. Repeats until the user quits or the deck is empty.
#
# Concepts practiced:
#     - Lists and tuples to represent cards and the deck
#     - Nested for loops to build the deck
#     - Functions with parameters and return values
#     - List comprehensions and the pop method
#     - Tuple unpacking
#     - While loops with break and continue
#     - Input validation with try / except
#     - The random module (shuffle)
#     - String formatting with f-strings (alignment)

import random


def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    random.shuffle(deck)
    return deck


def draw_cards(deck, num_of_cards):
    return [deck.pop() for _ in range(num_of_cards)]


def show_card(card):
    suit, rank = card  # Tuple Unpacking
    print(f"""
    +-------+
    |{rank:<7}|
    |       |
    |   {suit}   |
    |       |
    |{rank:>7}|
    +-------+
    """)


deck = create_deck()

while deck:
    try:
        num_cards = int(
            input(
                f"How many cards would you like to draw? (0 to quit, {len(deck)} remaining): "
            )
        )
    except ValueError:
        print("Please enter a valid number.")
        continue

    if num_cards == 0:
        print("Thanks for playing!")
        break

    if num_cards < 0:
        print("Please enter a positive number.")
        continue

    if num_cards > len(deck):
        print(f"Not enough cards! Only {len(deck)} cards remaining.")
        continue

    hand = draw_cards(deck, num_cards)

    print("\nYour hand:")

    for card in hand:
        show_card(card)

if not deck:
    print("The deck is empty! No more cards to draw.")
