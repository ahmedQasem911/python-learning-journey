# Food Order System
# -----------------
# A simple command-line program that lets a user browse menus from different
# cuisines and place a meal order.
#
# How it works:
#     1. The user chooses a cuisine (Italian, Egyptian, or Indian).
#     2. The program displays the available meals for that cuisine.
#     3. The user enters the meal name and the number of portions.
#     4. The program checks that the meal exists on the chosen menu and prints
#        an order confirmation, or an error message if it doesn't.
#
# Concepts practiced:
#     - Lists to store menu items
#     - Functions with parameters and return values
#     - Conditional logic (if / elif / else)
#     - Looping through lists
#     - User input handling (strip, lower, split/join for clean input)
#     - String formatting with f-strings

italian_food = ["pasta bolognese", "pepperoni pizza", "margherita pizza", "lasagna"]

egyptian_food = ["koshari", "ful medames", "taameya", "hawawshi", "molokhia"]

indian_food = ["curry", "chutney", "samosa", "naan"]


def display_available_meals(cuisine):
    if cuisine == "italian":
        print("Available Italian Meals:")
        for meal in italian_food:
            print(meal.title())
    elif cuisine == "egyptian":
        print("Available Egyptian Meals:")
        for meal in egyptian_food:
            print(meal.title())
    elif cuisine == "indian":
        print("Available Indian Meals:")
        for meal in indian_food:
            print(meal.title())
    else:
        print(
            "Sorry, that cuisine isn't available. Please choose Italian, Indian, or Egyptian."
        )


def find_meal(meal_name, menu):
    if meal_name in menu:
        return meal_name
    else:
        return None


def select_meal(meal_name, cuisine):
    if cuisine == "italian":
        return find_meal(meal_name, italian_food)
    elif cuisine == "egyptian":
        return find_meal(meal_name, egyptian_food)
    elif cuisine == "indian":
        return find_meal(meal_name, indian_food)
    else:
        return None


def create_summary(meal_name, portions, cuisine):
    order = select_meal(meal_name, cuisine)
    if order is not None:
        return f"Order confirmed! {portions} portion(s) of {meal_name.title()}. Enjoy your meal!"
    else:
        return "Sorry, that meal isn't available on the selected menu."


print("Welcome to the Food Order System!")

cuisine_input = (
    input("Which cuisine would you like to explore? (Italian, Indian, Egyptian): ")
    .strip()
    .lower()
)

if cuisine_input not in ["italian", "egyptian", "indian"]:
    print("Please restart and choose a valid cuisine.")
else:
    display_available_meals(cuisine_input)

    meal_input = " ".join(
        input("Enter the name of the meal you'd like to order: ")
        .strip()
        .lower()
        .split()
    )

    portions_input = input("How many portions would you like to order? ").strip()

    result = create_summary(meal_input, portions_input, cuisine_input)
    print(result)
