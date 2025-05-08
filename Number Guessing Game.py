import random
import os

def get_high_score(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return int(file.read())
            except:
                return None
    return None

def save_high_score(filename, score):
    with open(filename, 'w') as file:
        file.write(str(score))

def number_guessing_game():
    print("🎉 Welcome to the Enhanced Number Guessing Game! 🎉")

    filename = "high_score.txt"

    while True:
        # Choose difficulty
        print("\nSelect Difficulty Level:")
        print("1. Easy (0-150)")
        print("2. Medium (0-750)")
        print("3. Hard (0-2000)")

        try:
            difficulty = int(input("Enter 1, 2, or 3: "))
            if difficulty == 1:
                max_range = 150
            elif difficulty == 2:
                max_range = 750
            elif difficulty == 3:
                max_range = 2000
            else:
                print("Invalid selection. Try again.")
                continue
        except ValueError:
            print("Please enter a number (1, 2, or 3).")
            continue

        secret_number = random.randint(1, max_range)
        attempts = 0

        print(f"\nI'm thinking of a number between 1 and {max_range}.")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < 1 or guess > max_range:
                    print(f"Please guess a number between 1 and {max_range}.")
                    continue

                if guess < secret_number:
                    print("Too low! 📉")
                elif guess > secret_number:
                    print("Too high! 📈")
                else:
                    print(f"🎯 Correct! You guessed it in {attempts} attempts.")

                    high_score = get_high_score(filename)
                    if high_score is None or attempts < high_score:
                        print("🏆 New High Score!")
                        save_high_score(filename, attempts)
                    else:
                        print(f"📊 Current High Score: {high_score} attempts")

                    break
            except ValueError:
                print("❌ Please enter a valid number.")

        # Play again?
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye!")
            break

# Run the game
if __name__ == "__main__":
    number_guessing_game()
