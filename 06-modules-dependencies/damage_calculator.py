# Weapon Damage Calculator
# -----------------------
# A simple program that calculates the power attack of each weapon and
# displays the results in a table.
#
# How it works:
#     1. Stores the weapons and their damage values in a list.
#     2. Calculates each weapon's power attack by squaring its damage.
#     3. Collects the results and prints them as a formatted table.
#
# Requirements:
#     - Third-party package: tabulate (install it with: pip install tabulate)
#
# Concepts practiced:
#     - Importing built-in modules (math)
#     - Installing and using third-party packages (tabulate)
#     - Managing dependencies with pip
#     - Nested lists
#     - For loops
#     - Formatting tabular output

import math

from tabulate import tabulate

weapons = [["Sword", 5], ["Axe", 7], ["Wand", 4]]

results = []

for weapon in weapons:
    name = weapon[0]
    damage = weapon[1]
    power_attack = math.pow(damage, 2)
    results.append([name, damage, power_attack])

headers = ["Weapon", "Damage", "Power Attack"]

output = tabulate(results, headers)
print(output)
