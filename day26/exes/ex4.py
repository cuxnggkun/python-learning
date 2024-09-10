from functools import partial

read = partial(open, mode="r")

print(read("test.txt").read())
