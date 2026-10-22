# Number Analyzer Program
# -----------------------
# A simple program that analyzes a number and reports its basic properties.
#
# How it works:
#     1. Checks whether the number is odd or even.
#     2. Finds all the factors of the number.
#     3. Uses the factors to check whether the number is prime.
#     4. Prints the result of each step.
#
# Concepts practiced:
#     - Functions with parameters and return values
#     - Conditional logic (if / else)
#     - While loops
#     - Modulo operator (%)
#     - Lists and the append method
#     - String formatting with f-strings


def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


def get_factors(number):
    factors = []
    iteration_index = 1
    while iteration_index <= number:
        if number % iteration_index == 0:
            factors.append(iteration_index)
        iteration_index += 1
    print(f"The factors of {number} are: {factors}")
    return factors


def check_prime(number, factors):
    if len(factors) == 2:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


def analyze_number(number):
    check_odd_even(number)
    factors = get_factors(number)
    check_prime(number, factors)


analyze_number(51)
