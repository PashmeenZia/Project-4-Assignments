def main():
    # Ask the user for input
    curr_value = int(input("Enter a number: "))

    # Keep doubling the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print the value in the same line

# Run the program
if __name__ == "__main__":
    main()