Calculator App

A simple calculator application built with Python that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

Features
	•	Addition (+)
	•	Subtraction (-)
	•	Multiplication (*)
	•	Division (/)
	•	Handles invalid inputs gracefully
 Prerequisites

Ensure you have Python installed on your system. You can check by running:
python --version
If Python is not installed, download and install it from python.org.
Installation
	1.	Clone the repository:
 git clone https://github.com/your-username/calculator-app.git
cd calculator-app
	2.	Run the calculator:
 python calculator.py
 Usage
	•	The program prompts the user to enter two numbers and an operator.
	•	It then performs the selected operation and displays the result.
	•	Example usage:
 Enter first number: 10
Enter operator (+, -, *, /): *
Enter second number: 5
Result: 50
Code Example
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"Result: {num1 + num2}")
        elif operator == "-":
            print(f"Result: {num1 - num2}")
        elif operator == "*":
            print(f"Result: {num1 * num2}")
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
Contributing

Feel free to contribute by submitting issues or pull requests.

License

This project is open-source and available under the MIT License.

