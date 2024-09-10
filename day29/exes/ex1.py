def decorator(func):
    def inside(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return inside


def greet():
    print('hello')


greet = decorator(greet)

greet()
