with open("ex1.txt") as fo:
    cnt = 0

    for line in fo:
        cnt += 1

    if '\n' in line:
        cnt += 1

    print(cnt)
