def prime_num():
    for divided in range(2, 101):
        for num in range(2, divided):
            if divided % num == 0:
                break
        else:

            yield divided


p = prime_num()
print(next(p))
print(next(p))
