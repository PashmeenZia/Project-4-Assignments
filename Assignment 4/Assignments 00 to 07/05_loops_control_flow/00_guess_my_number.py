import random

def main():
    secret_number = random.randint(1, 50)  # Random number between 1 and 50
    print("🔢 I have picked a number between 1 and 50. Can you guess it?")

    while True:
        try:
            guess = int(input("🎯 Your guess: "))
            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 You got it! The secret number was: {secret_number}")
                break
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Start the game
if __name__ == '__main__':
    main()
