# Ask the user to type a number
num = int(input("Enter any number: "))

# Check if the number is divisible by 2 (i.e., even)
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    # If it's not divisible by 2, then it's odd
    print(f"{num} is an odd number")
