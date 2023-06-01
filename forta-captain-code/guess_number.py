# import additional pre-existing code that handles random numbers maths
import random

# computer guesses a number
computer_num = random.randrange(1, 101)

# greetings from computer
name = input("What is your name? Please enter: ").capitalize()
print(f"Hello, {name}! I'm thinking of a number from 1 to 100...")

# user tries to guess a computer's number
user_num = 0

# until user answered with right number...
while user_num != computer_num:
    # ...computer will ask user to make a guess
    user_input = input("Make your guess: ")
    user_num = int(user_input)

    # if user's number is higher or lower than computer's then say so
    if user_num > computer_num:
        print("Too big. Try again")
    elif user_num < computer_num:
        print("Too small. Try again")
    else:
        # if user is guessed right, congratulate user and end the script
        print(f"Your guess is correct, {name}. You win!")
