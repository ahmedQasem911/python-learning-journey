# Personal Information Checker
# ----------------------------
# A simple command-line program that collects personal information from the
# user and displays a formatted profile.
#
# How it works:
#     1. Asks for the user's name, birth year, country, the programming
#        language they are learning, and their favorite number.
#     2. Calculates the age from the birth year and the current year.
#     3. Prints a profile summary, including the favorite number doubled and
#        the data type of the age.
#     4. Prints eligibility results using comparison operators (18 or older,
#        younger than 60, exactly 25, different from 30).
#     5. Prints the user's age in 5 years as an extra challenge.
#
# Concepts practiced:
#     - Variables and user input
#     - Type conversion with int()
#     - Checking data types with type()
#     - Arithmetic operators
#     - Comparison operators (>=, <, ==, !=)
#     - The datetime module
#     - String formatting with f-strings
#     - Formatted output with center() and string repetition

from datetime import datetime

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("Personal Information Checker".center(LINE_WIDTH))
print("=" * LINE_WIDTH)
print()

user_name = input("Enter your full name: ")
user_age = datetime.now().year - int(input("Enter your birth year: "))
user_country = input("Enter your country: ")
user_programming_language = input("What programming language are you learning? ")
user_favorite_number = int(input("Enter your favorite number: "))

print()
print("=" * LINE_WIDTH)
print("User Profile".center(LINE_WIDTH))
print("=" * LINE_WIDTH)
print()

print(f"Welcome, {user_name}!")
print(f"You are {user_age} years old and live in {user_country}.")
print(f"You are currently learning {user_programming_language}.")
print(f"Your favorite number multiplied by 2 = {user_favorite_number * 2}")

print(f"\nAge data type: {type(user_age)}")

print()
print("=" * LINE_WIDTH)
print("Eligibility Results".center(LINE_WIDTH))
print("=" * LINE_WIDTH)
print()

print(f"18 or older: {user_age >= 18}")
print(f"Younger than 60: {user_age < 60}")
print(f"Exactly 25 years old: {user_age == 25}")
print(f"Different from 30: {user_age != 30}")

print()
print("-" * LINE_WIDTH)
print("Extra Challenge".center(LINE_WIDTH))
print("-" * LINE_WIDTH)
print()

print(f"Your Age in 5 years: {user_age + 5}")
