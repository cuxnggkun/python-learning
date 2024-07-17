a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
c = a

print(id(a), id(b))
print(a == b)
print(a is b)
print(id(a), id(c))
print(a == c)
print(a is c)
