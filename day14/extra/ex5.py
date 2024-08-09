new_list = []

with open("ex1.txt") as fo:
    for line in fo:
        new_list.append(line.strip())

print(new_list)