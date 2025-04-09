def main():
    # User se saal ka input lena
    year = int(input('Please input a year: '))

    # Leap year check karna
    if year % 4 == 0:  # Agar 4 se divisible hai
        if year % 100 == 0:  # Aur agar 100 se divisible hai
            if year % 400 == 0:  # Aur agar 400 se divisible hai
                print("That's a leap year!")
            else:  # 100 se divisible hai lekin 400 se nahi
                print("That's not a leap year.")
        else:  # 4 se divisible hai lekin 100 se nahi
            print("That's a leap year!")
    else:  # 4 se bhi divisible nahi hai
        print("That's not a leap year.")

# Program yahan se run hota hai
if __name__ == '__main__':
    main()
