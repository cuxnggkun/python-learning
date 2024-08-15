def numbers(number):
    return number >= 0


print(*filter(numbers, range(-5, 11)))
