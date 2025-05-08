def fibonacci_sequence():
    print("=== FIBONACCI GENERATOR ===")
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

    except ValueError:
        print("Invalid input. Enter a positive integer.")

fibonacci_sequence()
