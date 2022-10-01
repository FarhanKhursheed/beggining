import random

def guess(x):
        random_number = random.randint(1,x)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess the number between 1 and {x}: "))
            if guess < random_number:
                print("Try again. Too low")
            elif guess > random_number:
                print("Try again. Too high")

        print("Correct answer")

guess(10)