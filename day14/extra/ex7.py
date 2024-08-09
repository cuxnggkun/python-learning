new_list = []

with open("ex1.txt") as fo:
    words = fo.read().splitlines()
    max_len = len(words[0])

    for word in words[1:]:
        if max_len < len(word):
            max_len = len(word)

    for word in words:
        if len(word) == max_len:
            print(word)
