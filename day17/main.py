def func(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    return sum(args)


lst = (1, 2, 3, 4, 10, 11, 12)
d = {'a': 2, 'b': 3, 'c': 4}
print(func(*lst, **d))

# lst = {'a': 1, 'b': 2}
#
# *first, last = lst
#
# print(first)

numbers = [1, 2, 3, 4, 5]

print(1, 2, 3, 4, 5, sep=" | ")
