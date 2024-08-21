try:
    user = int(input("Please enter integer 1 to 10: "))
    if user > 10:
        raise ValueError("Your choice is invalid")
except ValueError:
    print("Please enter a valid integer between 1 and 10.")
