# Constants for messages
PROMPT = "What do you want? "
JOKE = """Here is a joke for you!  
Why do programmers prefer dark mode?  
Because light attracts bugs!"""
SORRY = "Sorry, I only tell jokes."

def main():
    user_input = input(PROMPT)  # Ask the user for input
    if user_input == "Joke":
        print(JOKE)  # Print the joke if input is "Joke"
    else:
        print(SORRY)  # Print sorry message if input is anything else

# Run the program
if __name__ == "__main__":
    main()