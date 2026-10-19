# Shopping List App
#
# Compares a planned shopping list with the items that were actually bought.
#
# How it works:
# 1. Builds a shopping list and edits it with common list methods:
#    append() adds an item, insert() adds one at a specific position,
#    indexing replaces an item, and pop() removes the last item.
# 2. Compares the final shopping list with the purchased list and reports
#    the items that were planned but not purchased.
# 3. Reports the items that were purchased but were not on the list
#    (impulse buys).

shopping_list = ["potato", "apple", "oil", "milk", "toilet paper"]

shopping_list.append("batteries")

shopping_list.insert(0, "chocolate")

shopping_list[0] = "dark chocolate"

shopping_list.pop()
print(f"Shopping list: {shopping_list}")

purchased_list = [
    "dark chocolate",
    "potato",
    "apple",
    "oil",
    "toilet paper",
    "fish fingers",
]

unavailable_items = []

for item in shopping_list:
    if item not in purchased_list:
        unavailable_items.append(item)

if len(unavailable_items) > 0:
    print(
        f"Here's a list of items on your shopping list that you did not purchase: {unavailable_items}"
    )
else:
    print("Good job! You bought everything on your shopping list!")

special_items = []

for item in purchased_list:
    if item not in shopping_list:
        special_items.append(item)

if len(special_items) > 0:
    print(
        f"Here's a list of items you purchased but were not on your shopping list: {special_items}"
    )
