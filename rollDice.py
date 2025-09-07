import random #allows random generaton 

roll = random.randint(1,6) #randomly select a number 1-6
guess = int(input("Guess the dice roll...\n"))

if guess != roll:
    print("Wrong. The computer rolled a " + str(roll) + ". Guess again.")
else:
    print("Correct! The computer rolled a " + str(roll) + ".")