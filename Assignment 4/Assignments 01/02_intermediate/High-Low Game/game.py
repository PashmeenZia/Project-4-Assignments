import random

NUM_ROUNDS = 5  # Number of rounds to play

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0  # Keep track of player's score

    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        choice = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Ensure valid input
        while choice not in ["higher", "lower"]:
            choice = input("Please enter either 'higher' or 'lower': ").strip().lower()

        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)
        
        print("Your score is now", your_score)
        print()
    
    # Final score evaluation
    print("Your final score is", your_score)
    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()