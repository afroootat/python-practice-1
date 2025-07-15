# Ask the user to enter the first number
num1 = float(input("Enter a number: "))

# Ask the user to enter the second number
num2 = float(input("Enter another number: "))

# Ask the user to choose an operation
operation = input("Enter an operation(+, -, *, /): ")

# Check what operation was chosen and do the calculation
if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    print(f"Result: {num1 / num2}")
else:
    # If the user types something other than +, -, *, /
    print("Enter a valid operation!")
