# Number Guessing Game
# --------------------
# A simple command-line game where the player tries to guess a secret number
# between 1 and 100.
#
# How it works:
#     1. The player chooses a difficulty level (easy, medium, or hard), which
#        sets the number of allowed attempts (10, 7, or 5).
#     2. The player enters guesses. Each guess is validated: it must be a
#        number between 1 and 100.
#     3. After each guess, the game says whether it is too high or too low,
#        and adds a hint when the guess is within 10 of the secret number.
#     4. The game ends when the player guesses correctly or runs out of attempts.
#     5. The player can then choose to play another round or quit.
#
# Concepts practiced:
#     - Variables and user input
#     - Input validation with while loops and isdigit()
#     - Nested while loops with break and continue
#     - while-else (runs when the loop ends without a break)
#     - Conditional logic (if / elif / else)
#     - Comparison and logical operators (and, or, not)
#     - The abs function
#     - String formatting with f-strings

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("NUMBER GUESSING GAME".center(LINE_WIDTH))
print("=" * LINE_WIDTH)

# Game initialization
secret_num = 33
attempts_counter = 0
keep_going = True

# Difficulty selection
print()
print("Select your difficulty level:")
print("Easy   - 10 attempts")
print("Medium - 7 attempts")
print("Hard   - 5 attempts")

difficulty_level = input("\nEnter difficulty level: ").lower()

while (
    difficulty_level != "easy"
    and difficulty_level != "medium"
    and difficulty_level != "hard"
):
    print("Invalid difficulty level!")
    difficulty_level = input("Please enter easy, medium, or hard: ").lower()

if difficulty_level == "easy":
    max_attempts = 10
elif difficulty_level == "medium":
    max_attempts = 7
elif difficulty_level == "hard":
    max_attempts = 5

print()
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Game loop
while keep_going:
    while attempts_counter < max_attempts:
        print()
        user_guess = input("Enter your guess: ")

        # Numeric input validation
        while not user_guess.isdigit():
            print("Invalid input! Please enter a number.")
            user_guess = input("Enter your guess: ")

        user_guessed_num = int(user_guess)

        # Range validation
        if user_guessed_num < 1 or user_guessed_num > 100:
            print("Invalid attempt! Your guess must be between 1 and 100.")
            continue

        attempts_counter += 1

        # Check the player's guess
        if user_guessed_num == secret_num:
            print()

            if attempts_counter == 1:
                print("Wow! You got it on your first attempt!")
            else:
                print("Congratulations! You guessed the number!")
                print(f"You won in {attempts_counter} attempts!")

            break

        elif user_guessed_num > secret_num:
            print("Too high! Try a smaller number.")

            if abs(secret_num - user_guessed_num) <= 10:
                print("You're getting close!")

        elif user_guessed_num < secret_num:
            print("Too low! Try a bigger number.")

            if abs(secret_num - user_guessed_num) <= 10:
                print("You're getting close!")

    else:
        print()
        print("You are out of tries!")
        print(f"The secret number is {secret_num}.")
        print(f"You tried {attempts_counter} times.")

    # Play again
    print()
    new_round = input("Would you like to play again? (yes/no): ").lower()

    while new_round != "yes" and new_round != "no":
        print()
        new_round = input("Please enter yes or no: ").lower()

    if new_round == "yes":
        attempts_counter = 0

    elif new_round == "no":
        keep_going = False
        print()
        print("Thanks for playing. Goodbye!")
