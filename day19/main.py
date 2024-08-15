def func(x):
    if isinstance(x, list):
        raise ValueError("x must be int")

    return x + 10


try:
    print(func(0))
except ValueError as e:
    print(e)

"""
1 2 3 4 5 6 7 8
7
8
3
"""
