# ----------------------------------------------------------
# Trivia Time
# A three-question trivia game. Each question offers two choices
# and is worth a different number of points (10, 20, and 30).
# Correct answers add to the player's score, wrong or invalid
# answers add nothing, and the final score out of 60 is printed
# at the end.
# ----------------------------------------------------------

print("------------------------- Trivia Time -------------------------")

player_score = 0

print("1. Which planet is known as the Red Planet? (Mars, Venus)")

answer = input("Enter your answer: ").lower()

if answer == "mars":
    player_score += 10
    print("Correct Answer!")
    print(f"Points: {player_score}")
elif answer == "venus":
    print("Not quite!")
else:
    print("Wrong input!")

print(
    "2. Which animal is the largest mammal in the world? (Blue whale, African elephant)"
)

answer = input("Enter your answer: ").lower()

if answer == "blue whale":
    player_score += 20
    print("Correct Answer!")
    print(f"Points: {player_score}")
elif answer == "african elephant":
    print("Not quite!")
else:
    print("Wrong input!")


print("3. Which country was the birthplace of the Renaissance? (Italy, France)")

answer = input("Enter your answer: ").lower()

if answer == "italy":
    player_score += 30
    print("Correct Answer!")
    print(f"Points: {player_score}")
elif answer == "france":
    print("Not quite!")
else:
    print("Wrong input!")

print(f"Your final score is {player_score} out of 60!")
