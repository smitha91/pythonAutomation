import random #allows for random generated selection

computer_choice = random.choice(['rock', 'paper', 'scissors']) #choices
user_choice = input("Choose rock, paper, or scissors\n")

if computer_choice == user_choice:
    print("TIE. Try again.")
elif user_choice == "rock" and computer_choice == "scissors":
    print("YOU WIN! The computer threw " + computer_choice + ".")
elif user_choice == "rock" and computer_choice == "paper":
    print("YOU LOSE! The computer threw " + computer_choice + ".")
elif user_choice == "paper" and computer_choice == "rock":
    print("YOU WIN! The computer threw " + computer_choice + ".")
elif user_choice == "paper" and computer_choice == "scissors":
    print("YOU LOSE! The computer threw " + computer_choice + ".")
elif user_choice == "scissors" and computer_choice == "paper":
    print("YOU WIN! The computer threw " + computer_choice + ".")
elif user_choice == "scissors" and computer_choice == "rock":
    print("YOU LOSE! The computer threw " + computer_choice + ".")
else:
    print("YOU LOSE! The computer threw " + computer_choice + ".")
