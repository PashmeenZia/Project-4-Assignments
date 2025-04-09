#Project 5: Count Down Timer In Python
#Description: Ek countdown timer hai jo user sa seconds main time input leta hai aur phir usko
#minute:second format main display karta hai

import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) # minutes aur seconds calculated ho rahy hain
        time_format = '{:02d}:{:02d}'.format(mins, secs) # MM:SS fornmate
        print(time_format, end='\r')
        time.sleep(1)#delay
        seconds -= 1
    print("00:00 \n Time's Up!")

# user input for timer
total_seconds = int(input("Enter time in second for countdown: "))
countdown_timer(total_seconds)

