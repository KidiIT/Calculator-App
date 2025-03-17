# Simple Calculator project with Python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+,-,*, /,//) : ")

if operation == "+":
    print(f"Result: {num1 + num2}")
elif operation == "-":
    print(f"Result: {num1 - num2}")
elif operation == "*":
    print(f"Result: {num1 * num2}")
elif operation == "//":
    print(f"Results: {num1 // num2}")
elif operation == "/":
    if num2 != 0:
            print(f"Result: {num1 / num2}")
    else:
        print("Error: Division by Zero is not allowed.")
else:
    print("Invalid operation")
    