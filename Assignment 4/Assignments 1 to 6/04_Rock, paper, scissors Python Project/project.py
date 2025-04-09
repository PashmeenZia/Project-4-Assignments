# Project 4: Rock, Paper, Scissors Game

import random

#game choices
choices = ["rock", "paper", "scissors"]

#player choice

player_choice = input("Enter rock, paper, or scissors: ").lower()

#computer choice
computer_choice = random.choice(choices)

#winner decision
if player_choice == computer_choice:
    print(f"dono ka choice {player_choice} the . Its a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "paper" and computer_choice == "rock":
    print(f"Players wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Players wins! {player_choice} beats {computer_choice}.")

else:
    print(f"Computer Wins! {computer_choice} beats {player_choice}.")