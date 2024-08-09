def get_all(*args, **kwargs):
    print("Positional arguments")
    for x in args:
        print(x)

    print("Keyword arguments")
    for key, value in kwargs.items():
        print(key, value, sep=" ")


get_all(1, 2, a=1, b=2)
