import random 

userInput=""
userGuess=0
userPoints=0

randNum = random.randrange(1, 101)

print("I am thinking of a number between 1 and 100")

while randNum != userGuess:
    
    userInput=input("Your guess:").strip()

    if not userInput.isnumeric():
        print(userInput, "is not a valid number")
    else:
        userGuess=int(userInput)

        if userGuess < randNum:
            print("Too low. Try again")
            userPoints += 1
        elif userGuess > randNum:
            print("Too high. Try again.")
            userPoints += 1
        else:
            print("You got it!")

print("Thanks for playing! Your score is", userPoints)
