# ----------------------------------------------------------
# Simple Calculator
# Asks the user for two numbers and an operation (+, -, *, /),
# then prints the result.
# ----------------------------------------------------------

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("Calculator".center(LINE_WIDTH))
print("=" * LINE_WIDTH)
print()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Wrong entered operation!")
