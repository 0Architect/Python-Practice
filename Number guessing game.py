import math
import random

print("Hello user, welcome to the guessing game!")

difficulty_level = 0
while True:
    try:
        difficulty_level = int(input("Please pick a difficulty level (1-3): "))
        if(difficulty_level < 1 or difficulty_level > 3):
            raise ValueError
        break
    except ValueError:
        print("Please input an integer and ensure it is from 1 - 3")

if(difficulty_level == 1):
    guess_range = 10
elif(difficulty_level == 2):
    guess_range = 50
else:
    guess_range = 100

no_of_tries = math.ceil(math.log2(guess_range))
no_of_tries += (difficulty_level != 3) * 2

print(f"Okay Let's begin!\nI am thinking of a number between 1 and {guess_range}\n You are to guess my number in {no_of_tries} tries")

user_guess = 0
answer = random.randint(1, guess_range)

while(user_guess != answer and no_of_tries > 0):
    no_of_tries -= 1
    while(True):
        try:
            user_guess = int(input("What's your guess?: "))
            if(user_guess < 1 or user_guess > guess_range):
                raise ValueError
            break
        except ValueError:
            print(f"Please input an integer and ensure it is from 1 - {guess_range}")
    if(user_guess < answer):
        print(f"Too low! You have {no_of_tries} left")
    elif(user_guess > answer):
        print(f"Too high! You have {no_of_tries} left")

if (user_guess != answer):
    print(f"You lost! The correct number was {answer} Try again!")
else:
    print("You are brilliant, you won!")