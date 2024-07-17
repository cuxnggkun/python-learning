#                0     1       2           3     4            -            index/position
# 3 = 4 - 1 = len - 1
# 4 = 5 - 1 = len - 1
#                -5    -4       -3        -2     -1           - index/position
friend_names = ["Ha", "Nam", "Phuong", "Dang", "Danh"]  # value

print(len(friend_names))

print(friend_names[0])
print(friend_names[len(friend_names) - 1])

print(friend_names[-len(friend_names)])
print(friend_names[-1])

print(friend_names[len(friend_names) // 2])

friend_names[0] = "Dung"
print(friend_names)

friend_names[-1] = "cuong"
print(friend_names)

friend_names.append("Quang")
print(friend_names)

friend_names.extend(["Cuong2", "Cuong3"])
print(friend_names)

friend_names.insert(0, "Hoa")
print(friend_names)

friend_names.insert(-1000, "Linh")
print(friend_names)

friend_names.remove("Linh")
print(friend_names)

del friend_names[2]
print(friend_names)

print(friend_names.pop(-3))
print(friend_names)

print(friend_names.pop())
print(friend_names)

print(friend_names.index("cuong"))
print(friend_names.count("Cuong100"))
friend_names.reverse()

print(friend_names)

friend_names.sort()
print(friend_names)
