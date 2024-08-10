import random

secret = random.randint(1, 100)

guess = int(input("Please enter your guess: "))

while guess != secret:
    if guess > secret:
        print("Your number is higher.")
    else:
        print("Your number is lower")
    guess = int(input("Please enter your guess: "))

print("Correct")
