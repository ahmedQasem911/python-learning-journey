# ----------------------------------------------------------
# Introduction Chatbot
# A simple program that asks for the user's name, age, and
# favorite color, then responds to each answer.
# ----------------------------------------------------------

name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")

age = int(input("How old are you? "))
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")