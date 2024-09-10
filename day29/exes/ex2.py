books = []


def decorator(func):
    def require(books):
        if len(books) != 0:
            func(books)

    return require


@decorator
def get_book(books):
    print(books)


get_book([])
