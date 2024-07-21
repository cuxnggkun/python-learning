secret_num = 50

guess = int(input("Please guess the number: "))

while guess != secret_num:
    print("Wrong!")
    secret_num = int(input("Please select again: "))

print("Correctly!")
