def calculator():
    print("\n=== BASIC CALCULATOR ===")
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

def fibonacci_sequence():
    print("\n=== FIBONACCI SEQUENCE GENERATOR ===")
    try:
        n = int(input("Enter how many terms you want: "))
        a, b = 0, 1
        if n <= 0:
            print("Please enter a positive integer.")
        elif n == 1:
            print("Fibonacci Sequence: 0")
        else:
            print("Fibonacci Sequence:")
            for _ in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()
    except ValueError:
        print("Invalid input. Enter a positive integer.")

def palindrome_checker():
    print("\n=== PALINDROME CHECKER ===")
    text = input("Enter a word or number: ")
    clean_text = text.replace(" ", "").lower()
    reversed_text = clean_text[::-1]
    if clean_text == reversed_text:
        print(f"'{text}' is a palindrome.")
    else:
        print(f"'{text}' is not a palindrome.")

def armstrong_checker():
    print("\n=== ARMSTRONG NUMBER CHECKER ===")
    try:
        num = int(input("Enter a number: "))
        digits = str(num)
        power = len(digits)
        total = sum(int(d)**power for d in digits)

        if total == num:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")

def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Basic Calculator")
        print("2. Fibonacci Sequence Generator")
        print("3. Palindrome Checker")
        print("4. Armstrong Number Checker")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            calculator()
        elif choice == '2':
            fibonacci_sequence()
        elif choice == '3':
            palindrome_checker()
        elif choice == '4':
            armstrong_checker()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu
main()
