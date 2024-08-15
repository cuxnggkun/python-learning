try:
    with open("data.txt") as fo:
        print(fo.read())
except FileNotFoundError as e:
    print(e)
