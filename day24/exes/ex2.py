def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as Z:
        print(f"Error: {Z}")
    except TypeError as T:
        print(f"Error: {T}")
    except ArithmeticError as A:
        print(f"Error: {A}")

divide(123, 2)