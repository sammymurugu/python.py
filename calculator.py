def calculate():
    """
    Prompts the user for two numbers and an operator, performs the calculation, and prints the result.
    """

    # Get input from the user
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter numbers.")

    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            break  # Exit the loop if the operator is valid
        else:
            print("Invalid operator. Please enter +, -, *, or /.")

    # Perform the calculation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    # Print the result
    print(f"{num1} {operator} {num2} = {result}")

# Run the calculator
calculate()