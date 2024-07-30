def add(num1, num2):
    print("Add:", num1 + num2)


def subtract(num1, num2):
    print("Subtract:", num1 - num2)


def divide(num1, num2):
    if num2 == 0:
        print("Zero division")
    else:
        print("Divide:", num1 / num2)


def multiply(num1, num2):
    print("Multiply:", num1 * num2)


add(1, 2)
subtract(6, 2)
divide(10, 2)
multiply(5, 2)
