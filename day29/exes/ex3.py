def printer(func):
    def inner(*args, **kwargs):
        x = func(*args, **kwargs)
        if x is not None:
            print(x)
    return inner


@printer
def greet():
    return None


greet()
