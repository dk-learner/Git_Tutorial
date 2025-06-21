import random

def guessing_game():
    secret = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        print("Congratulations! You guessed the number.")
    else:
        print(f"Sorry, the correct number was {secret}. Try Again!")

guessing_game()