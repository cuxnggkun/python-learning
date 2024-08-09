from pprint import pprint


def add(x, y):
    print(locals())
    return x + y


add(1, 2)