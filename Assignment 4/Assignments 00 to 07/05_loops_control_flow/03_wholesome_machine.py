def main():
    affirmation = "I believe in myself and my abilities."
    print(f"🌟 Please type the following affirmation exactly as shown:\n👉 {affirmation}")

    while True:
        user_input = input("\033[32m")  # Green color input
        print("\033[0m", end="")  # Reset color to default

        if user_input == affirmation:
            print("✅ Perfect! You typed it right. Keep believing in yourself! 💪")
            break
        else:
            print(f"❌ Oops! That wasn't quite right.\nPlease type the affirmation again:\n👉 {affirmation}")

# Standard way to run the program
if __name__ == '__main__':
    main()
