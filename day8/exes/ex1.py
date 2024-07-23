import random

secret_num = random.randint(1, 100)

guess = int(input("Please guess the number: "))

while guess != secret_num:
    if guess > secret_num:
        print("Your number is higher than secret number.")
    else:
        print("Your number is lower than secret number.")
    guess = int(input("Please select again: "))

print("Correctly!")
