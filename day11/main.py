s1 = set()

print(len(s1))

s2 = {1, 4, 4, 3, 2}

print(s2)

s1.add(100)
s1.update("abc")
s1.update([4, 5, 6])
print(s1)

s1.remove(100)
print(s1.pop())
s1.discard(4)
print(s1)

print(s1.copy())
# s1.clear()

print(s1)

set_a = {4, 5}
set_b = {100, 101, 102, 4, 5}

print(set_a.difference(set_b))
print(set_b.difference(set_a))
print(set_a.intersection(set_b))

print(set_a.symmetric_difference(set_b))
print(set_a.union(set_b))
print(set_a - set_b)
print(set_b - set_a)
print(set_b & set_a)
print(set_a | set_b)
print(set_a ^ set_b)

print(set_a.issubset(set_b))
