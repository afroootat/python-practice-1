num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operation = input("Enter an operation(+, -, *, /): ")

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Enter a valid operation!")