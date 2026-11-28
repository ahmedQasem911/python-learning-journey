# ----------------------------------------------------------
# Rock, Paper, Scissors (Best of Three)
# Plays rock, paper, scissors against the computer, which picks
# its move at random. Ties don't count, and the first side to
# win two rounds wins the match. Invalid inputs are rejected
# and the round is replayed.
# ----------------------------------------------------------

import random

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("Rock, Paper, Scissors (Best of Three)".center(LINE_WIDTH))
print("=" * LINE_WIDTH)

player_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while player_wins < 2 and computer_wins < 2:
    print()
    player_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        winner = "Player"
    elif player_choice == computer_choice:
        winner = "Tie"
    else:
        winner = "Computer"

    if winner == "Player":
        player_wins += 1
        print("You won")
    elif winner == "Computer":
        computer_wins += 1
        print("Computer won")
    else:
        print("It's a tie")

    print("=" * LINE_WIDTH)
    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")
    print()

if player_wins > computer_wins:
    print("Congratulations! You won.")
else:
    print("Computer won!")
