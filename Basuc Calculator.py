def calculator():
    print("=== BASIC CALCULATOR ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Choose operation (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

calculator()

