FILE_LOG = "log.txt"


def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except LookupError as le:
        with open(FILE_LOG, "a") as fo:
            fo.write(f"Error: {le} \n")
            raise
    finally:
        print("Done Run")


itemgetter([1, 2, 3, 4], 6)
